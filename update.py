from django.template import loader, Context
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from NFL_App.media._help import nfl_teams
from NFL_App.media._help import weeks_to_date
from Select.models import game_week, game_pick, user
from collections import Counter

import sys

def render_email(breakdown, winners):
    email_template = loader.get_template('email.html')
    email_context = Context({
        'players' : breakdown,
        'winners' : winners,
    })
    rendered = email_template.render(email_context)

    return rendered

def update_scores(current_week, games, mocked_data):
    home_team_nam = nfl_teams.switch_find_team_by_abbr(mocked_data[games]['home']['abbr'])
    game_obj = game_week.objects.filter(week=current_week).filter(home_team=home_team_nam)
    this_game = game_obj[0]
    this_game.home_score = mocked_data[games]['home']['score']['T']
    this_game.away_score = mocked_data[games]['away']['score']['T']
    this_game.save()
    game_obj_retry = game_week.objects.filter(week=current_week).filter(home_team=home_team_nam)

def update_game_score(curr_week):
    mocked_data = weeks_to_date.get_json()
    current_week = curr_week
    for games in mocked_data.keys():
        try:
            if not 'Final' in mocked_data[games]['qtr']:
                update_scores(current_week, games, mocked_data)
            else:
                update_scores(current_week, games, mocked_data)
                home_team_nam = nfl_teams.switch_find_team_by_abbr(mocked_data[games]['home']['abbr'])
                game_obj = game_week.objects.filter(week=current_week).filter(home_team=home_team_nam)
                home_score, away_score = game_obj[0].home_score, game_obj[0].away_score
                winner = 0 if home_score > away_score else 1
                x = game_pick.objects.filter(game_weeks__week=curr_week)
                for game_played in x.filter(game_weeks__home_team=home_team_nam):
                    if winner == game_played.pick:
                        game_played.won = 'W'
                        game_played.save()
                        user_object = user.objects.get(id=game_played.user_id)
                        tac_win = user_object.wins
                        user_object.wins = tac_win + 3
                        user_object.save()
                    else:
                        game_played.won = 'L'
                        game_played.save()
                        user_object = user.objects.get(id=game_played.user_id)
                        tac_loss = user_object.loses
                        user_object.loses = tac_loss + 1
                        user_object.save()
        except TypeError:
            pass

    winner = ['', 0]
    breakdown = []
    for usr in user.objects.all():
        usr_wins = Counter()
        for game in game_pick.objects.filter(game_weeks__week=curr_week).filter(user_id=usr.id):
            usr_wins.update(game.won)
        if usr_wins['W'] == winner[1]:
            winner[0] += winner[0][-1:0] + ',' + str(usr.user_name)
        elif usr_wins['W'] > winner[1]:
            winner[0] = str(usr.user_name)
            winner[1] = usr_wins['W']
        wins = 0 if not usr_wins['W'] else usr_wins['W']
        loses = 0 if not usr_wins['L'] else usr_wins['L']
        breakdown.append([str(usr.user_name), wins, loses])

    winners = ""
    # Update User with total weeks won
    try:
        winner = user.objects.get(user_name=winner[0])
        winner.total_week_wins += 1
        winner.save()
    except user.DoesNotExist:
        winners = winner[0].split(',')
        for add_win in winners:
            one_winner = user.objects.get(user_name=add_win)
            one_winner.total_week_wins += 1
            one_winner.save()

    mass_usrs = [str(x.email) for x in User.objects.all() if x.email]
    msg_header = 'NFL - Martin Picks Summary'

    if winners:
        winner = winners[0]

    msg_body = render_email(breakdown, winner)
    from_email = 'DoNotReply@NFLApp.com'

    msg = EmailMessage(msg_header, msg_body, from_email, mass_usrs)
    msg.content_subtype = "html"
    msg.send()

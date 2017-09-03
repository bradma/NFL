from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import game_pick, game_week, user
from Select.forms import pick_week_one_games

def review_content(request, user_id, week_id):
    template_name = 'user_show_week_content.html'
    all_playable_games = game_week.objects.filter(week=week_id).order_by('id')
    context = {}
    return render(request, template_name, context)

def save_picks(request, picked_games, user):
    items = request.body.decode('utf-8').split('&')
    for updates in items:
        if 'game' in updates and not updates[updates.index('=')+1:] == 3:
            index_g = updates[updates.index('e')+1:updates.index('=')]
            update_with = int(updates[updates.index('=')+1:])
            index_id_for_game = int(index_g)
            grab_game = game_pick.objects.filter(game_weeks=index_id_for_game).get(user=user)
            grab_game.pick = update_with
            grab_game.save()

@login_required
def success_submit(request, user_id, week_id):
    template_name = 'select_week_success_submission.html'
    if request.method == 'POST':
        all_playable_games = game_week.objects.filter(week=week_id).order_by('id')
        save_picks(request, all_playable_games, user_id)
    my_user = user.objects.get(id=user_id)
    selected_games = game_pick.objects.filter(game_weeks_id__week=week_id).filter(user_id=user_id)
    my_user = selected_games[0].user.user_name
    context = {
        'user_id' : user_id,
        'user' : my_user,
        'games' : selected_games
    }
    return render(request, template_name, context)

@login_required
def select_game_week_one(request, week_id, **args):
    template_name = 'select_week_one_games.html'
    week = game_pick.objects.filter(game_weeks__week=week_id)
    all_playable_games = ''
    games_all_picked = len([x for x in week if x.pick == 3])
    if games_all_picked > 0:
        all_playable_games = game_week.objects.filter(week=week_id).order_by("id")
    form = pick_week_one_games(pass_games=all_playable_games, user_id=args['user_id'])
    context = {
        'user' : args['user_id'],
        'week' : week_id,
        'playable_games' : all_playable_games,
        'form' : form,
        'game_all_picked' : games_all_picked
    }
    return render(request, template_name, context)

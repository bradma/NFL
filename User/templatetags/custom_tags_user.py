from django import template

from Select.models import game_pick, user

register = template.Library()

@register.tag(name="find_this_week")
def do_find_this_week(parser, token):
    try:
        tag_name, week_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return CurrentWeekNode(week_string)

class CurrentWeekNode(template.Node):
    def __init__(self, format_string):
        self.format_string = template.Variable(format_string)

    def render(self, context):
        actual_format_string = self.format_string.resolve(context)
        _html = create_html(actual_format_string)
        return _html

def create_html(select_this_week):
    base = '<table><thead><th>Games</th>'
    players = user.objects.all().order_by('id')
    for object_players in players:
        base += '<th>' + object_players.user_name + '</th>'
    else:
        base += '</thead><tbody>'
    left_handled_games = game_pick.objects.filter(game_weeks__week=select_this_week).distinct('game_weeks')
    for c, title_games in enumerate(left_handled_games, start=1):
        base += '<tr><td>' + str(title_games.game_weeks) + '</td>'
        team_q_args = str(title_games.game_weeks.home_team)
        player_picked_games = game_pick.objects.filter(game_weeks__week=select_this_week).filter(game_weeks__home_team=team_q_args).order_by('user_id')
        for player_games in player_picked_games:
            if player_games.pick == 0:
                base += '<td>' + player_games.game_weeks.home_team + '</td>'
            elif player_games.pick == 1:
                base += '<td>' + player_games.game_weeks.away_team + '</td>'
            elif player_games.pick == 3:
                base += '<td>Game Never Picked</td>'
        else:
            base += '</tr>'
    else:
        base += '</tbody></table>'
    return base

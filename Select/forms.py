from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from Select.models import game_pick

from NFL_App.media._help import nfl_teams

class HorizontalRadioRender(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class pick_week_one_games(forms.Form):
    def __init__(self, *args, **kwargs):
        games = kwargs.pop('pass_games')
        myUser = kwargs.pop('user_id')
        super(pick_week_one_games, self).__init__(*args, **kwargs)
        for (position, game) in enumerate(games, start=1):
            time = 'time_' + str(position)
            location = 'location_' + str(position)
            #import pdb; pdb.set_trace()
            #home = str(game).split(" vs ")[0]
            #away = str(game).split(" vs ")[1]
            home, away = game.home_team, game.away_team
            home_img = nfl_teams.switch_find_img(home)
            away_img = nfl_teams.switch_find_img(away)
            HOME_TEAM = format_html('{0}\t{1}', home_img, home)
            AWAY_TEAM = format_html('{0}\t{1}', away_img, away)
            GAME_ONE = (
                (0, HOME_TEAM),
                (1, AWAY_TEAM),
            )
            game_id = 'game' + str(game.id)
            game_label = 'Game ' + str(position)
            self.fields[game_id] = forms.ChoiceField(choices=GAME_ONE, label=game_label, widget=forms.RadioSelect(renderer=HorizontalRadioRender))
            self.fields[time] = forms.CharField(label=game.time, widget=forms.HiddenInput())
            self.fields[location] = forms.CharField(label=game.location, widget=forms.HiddenInput())
            if not game_pick.objects.filter(game_weeks_id=game.pk).get(user_id=myUser).pick == 3:
                self.fields[game_id].widget.attrs['disabled'] = True
                self.fields[time].widget.attrs['disabled'] = True
                self.fields[location].widget.attrs['disabled'] = True

from Select.models import user, game_week, game_pick
import pickle

schedule = pickle.load(open('2016_schedule.p', "rb"))
users = user.objects.all()
for (i, curr_week) in enumerate(schedule, start=1):
    for game in curr_week:
        game_week_info = {
            'home_team': game['home_team'],
            'away_team': game['away_team'],
            'time': game['game_time'],
            'location': game['location'],
            'week': i
        }
        game_obj = game_week.objects.create(**game_week_info)
        for user in users:
            game_pick_info = {
                'pick': 3,
                'game_weeks': game_obj,
                'user': user,
            }
            game_pick.objects.create(**game_pick_info)

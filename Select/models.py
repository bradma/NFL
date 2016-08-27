from django.db import models

#Select App
class user(models.Model):
    user_name = models.CharField(max_length=10,)
    wins = models.IntegerField(max_length=20, default=0)
    loses = models.IntegerField(max_length=20, default=0)
    total_week_wins = models.IntegerField(max_length=20, default=0)
    team_name = models.CharField(max_length=20, null=True)

    class Meta:
        ordering = ["-total_week_wins"]

    def __unicode__(self):
        return self.user_name

class game_week(models.Model):
    home_team = models.CharField(max_length=30,)
    away_team = models.CharField(max_length=30,)
    time = models.CharField(max_length=30,)
    location = models.CharField(max_length=30,)
    week = models.IntegerField(max_length=20,)
    home_score = models.IntegerField(max_length=20, default=0, null=True)
    away_score = models.IntegerField(max_length=20, default=0, null=True)

    def __unicode__(self):
        return ' vs '.join([
            self.home_team,
            self.away_team,
        ])

class game_pick(models.Model):
    pick = models.IntegerField(max_length=2,)
    game_weeks = models.ForeignKey(game_week)
    user = models.ForeignKey(user)
    won = models.CharField(max_length=1, default='P')

    def __unicode__(self):
        return ' '.join([
                'Pick',
                str(self.pick),
                'User',
                self.user.user_name,
                'Week',
                str(self.game_weeks.week)
            ])

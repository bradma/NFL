from django.test import TestCase

from Select.models import user, game_week, game_pick

class model_user_test_cases(TestCase):
	def setUp(self):
		user.objects.create(id=0, user_name='Tester', wins=1, loses=3)
		user.objects.create(id=3, user_name='TesterTwo', wins=2, loses=5)
		game_week.objects.create(
			home_team='Eagles', 
			away_team='Cowboys', 
			time='1:00 PM', 
			location='Lincoln Finacial', 
			week=1
		)
		game_week.objects.create(
			home_team='Titans',
			away_team='Raiders',
			time='4:00 PM',
			location='Black Hole',
			week=2
		)
		_game_week = game_week(
			id=0,
			home_team='Eagles',
			away_team='Cowboys',
			time='2:00PM',
			location='Cowboys Stadium',
			week=1
		)
		_user = user(id=0, user_name='TestPicks', loses=1, wins=20)
		#Added remove if needed
		game_week.objects.create(
			id=1,
			home_team='Eagles',
			away_team='Cowboys',
			time='2:00PM',
			location='Cowboys Stadium',
			week=1
		)
		game_week.objects.create(
			id=10,
			home_team='Team1',
			away_team='Team2',
			time='3:00 PM',
			location='Linc',
			week=1,
			home_score=20,
			away_score=14
		)
		game_pick.objects.create(
			id=1,
			pick=1,
			game_weeks=_game_week,
			user=_user
		)

	def test_user_query(self):
		get_name = user.objects.get(id=0)
		get_wins = get_name.wins
		get_loses = get_name.loses
		self.assertEquals(str(get_name.user_name), 'Tester', 'Select username query is not working')
		self.assertEquals(get_wins, 1, 'Select user query for wins is not working')
		self.assertEquals(get_loses, 3, 'Select user query for loses is not working')

	def test_game_weeks_basic_query(self):
		games = game_week.objects.filter(week=1).order_by('id')
		homeTeam = games[0].home_team
		awayTeam = games[0].away_team
		_time = games[0].time
		_location = games[0].location
		_week = games[0].week
		actual_unicode = 'Basic games_week uniccode is wrong. Actual: ', str(games)
		self.assertEquals(str(games), '[<game_week: Eagles vs Cowboys>]', actual_unicode)
		self.assertEquals(str(homeTeam), 'Eagles', 'Basic games_week query for home_team is not working')
		self.assertEquals(str(awayTeam), 'Cowboys', 'Basic games_week query for away_team is not working')
		self.assertEquals(str(_time), '1:00 PM', 'Basic games_week query for time is not working')
		self.assertEquals(str(_location), 'Lincoln Finacial', 'Basic games_week query for location is not working')
		self.assertEquals(_week, 1, 'Basic games_week query for week is not working')

	def test_game_weeks_scores(self):
		game = game_week.objects.get(id=10)
		self.assertEquals(game.home_team, 'Team1', 'Team is not showing correctly')
		self.assertEquals(game.home_score, 20, 'Team1 score is not showing correctly')
		self.assertEquals(game.away_score, 14, 'Team2 score is not showing correctly')

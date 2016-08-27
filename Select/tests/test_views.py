from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User, AnonymousUser

from Select.views import select_game_week_one, success_submit
from Select.models import user, game_week, game_pick
from Select.forms import pick_week_one_games

class Select_views_tests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user_auth = User.objects.create_user(
			username='tester',
			password='Happy123'
		)
		user.objects.create(
			id = '2',
			user_name='tester',
			wins=2,
			loses=1,
			total_week_wins=1
		)
		game_week.objects.create(
			id='1',
			home_team='Tennessee Titans',
			away_team='Pittsburgh Steelers',
			time='1:00 PM',
			location='Hines Field',
			week=1
		)
		game_pick.objects.create(
			pick=3,
			user_id=2,
			game_weeks_id=1
		)

	def test_select_game_week_view_available_valid_user(self):
		request = self.factory.get('/User/WeekOne/2/1/')
		request.user = self.user_auth
		response = select_game_week_one(request, user_id=2, week_id=1)
		self.assertEqual(response.status_code, 200, 'Valid user is not able to navigate to select week one page')
		if not 'Pittsburgh Steelers' in response.content:
			assert False, 'Content does not appear to be rendering correctly, please check'
		if not 'Tennessee Titans' in response.content:
			assert False, 'Content does not appear to be rendering correctly please check'

	def test_select_game_week_view_available_invalid_user(self):
		request = self.factory.get('/User/WeekOne/2/1')
		request.user = AnonymousUser()
		response = select_game_week_one(request, user_id=2, week_id=1)
		self.assertEqual(response.status_code, 302, 'Anonymous User is able to access content on Select Week ones!')

	def test_select_game_successful_submit_valid_user(self):
		request = self.factory.get('/User/WeekOne/2/1/weekSubmit/')
		request.user = self.user_auth
		response = success_submit(request, user_id=2, week_id=1)
		self.assertEqual(response.status_code, 200, 'Successful submit page is not rendering correctly')
	
	def test_select_game_successful_submit_invalid_user(self):
		request = self.factory.get('/User/WeekOne/2/1/weekSubmit/')
		request.user = AnonymousUser()
		response = success_submit(request, user_id=2, week_id=1)
		self.assertEqual(response.status_code, 302, 'Anonymous User is able to access content on successful Submit')

	def test_form_function(self):
		all_playable_games = game_week.objects.filter(week=1).order_by('id')
		form = pick_week_one_games(pass_games=all_playable_games, user_id=2)
		self.assertFalse(form.is_valid())
		self.assertEqual(form.__dict__['fields']['time_1'].label, '1:00 PM', 'Form label for time is incorrect or not showing')
		self.assertEqual(form.__dict__['fields']['location_1'].label, 'Hines Field', 'Form label for location is incoorect or not showing')
		self.assertEqual(form.__dict__['fields']['game1'].choices[0][0], 0, 'Value for home team is incorrect or not displaying correctly')
		if not 'Tennessee Titans' in form.__dict__['fields']['game1'].choices[0][1]:
			assert False, 'Home team is invalid'
		self.assertEqual(form.__dict__['fields']['game1'].choices[1][0], 1, 'Value for away team is incorrect or not displaying correctly')
		if not 'Pittsburgh Steelers' in form.__dict__['fields']['game1'].choices[1][1]:
			assert False, 'Away team is invalid'


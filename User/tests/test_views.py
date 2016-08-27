from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser

from User.views import main_user
from Select.models import user

class User_view_tests(TestCase):
	def setUp(self):
		self.user_auth = User.objects.create_user(
			username='tester',
			password='Happy123'
		)
		user.objects.create(
			id='1',
			user_name='tester',
			wins=2,
			loses=1,
			total_week_wins=2,
		)

	def test_User_Main_valid(self):
		request = self.client.get('/User/1/')
		request.user = self.user_auth
		response = main_user(request, 1)
		self.assertEqual(response.status_code, 200, 'Login Home page is not displaying')

	def test_User_Main_invalid_user(self):
		request = self.client.get('/User/1/')
		request.user = AnonymousUser()
		response = main_user(request, 1)
		self.assertEqual(response.status_code, 403, 'Login Home page is allowing invalid users in')
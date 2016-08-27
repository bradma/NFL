from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

from User.views import main_user
from Select.models import user

class NFL_APP_tests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user_auth = User.objects.create_user(
			username='tester',
			password='Happy123'
		)
		user.objects.create(
			id='3',
			user_name='tester',
			wins=0,
			loses=0,
			total_week_wins=0
		)

	def test_login_site_available(self):
		response = self.client.get('')
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'), 'Login site is missing proper html5 tag')
		self.assertEqual(response.status_code, 200, 'Login Home page is not displaying')

	def test_login_site_login_valid_user(self):
		request = self.factory.get('/User/3')
		request.user = self.user_auth
		response = main_user(request, self.user_auth.id)
		self.assertEqual(response.status_code, 200, 'User Main Login for user tester is not working correctly')
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'), 'Login valid user is missing proper html5 tag')

	def test_login_site_login_invalid_user(self):
		request = self.factory.get('/User/2')
		request.user = AnonymousUser()
		response = main_user(request, 2)
		self.assertEqual(response.status_code, 403, 'User Main showed when it shouldnt be as user is AnonymousUser')
		if not 'Restricted' in response.content:
			assert False, 'Restricted user message is not displaying'

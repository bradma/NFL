from django.test import TestCase
from django.contrib.auth.models import User

from User.forms import change_password, add_team

class test_user_forms(TestCase):
	def setUp(self):
		self.user_auth = User.objects.create(
			username='tester',
			password='Happy123'
		)

	def test_change_password_form(self):
		form = change_password({
			'password' : 'Happy123',
			'newpassword' : 'happy999',
		})
		self.assertTrue(form.is_valid(), 'Form is not validating arguments')
		self.assertEqual(form.__dict__['data']['password'], 'Happy123', 'Old password is being captured correctly by form')
		self.assertEqual(form.__dict__['data']['newpassword'], 'happy999', 'Form is not accepting arguments correctly!')

	def test_change_password_value(self):
		form = change_password({
			'newpassword' : 'happy999',
		})
		self.user_auth.set_password(form.__dict__['data']['newpassword'])
		self.user_auth.save()

	def test_team_name_negative_boundary(self):
		form = add_team({
			'teamName' : 'asdfkljasdfkljzxclkjkldsfjas;dfjas;dfjas;dfjasdk;lfjas;dfjadsf'
			})
		self.assertFalse(form.is_valid(), 'Form rules for max length are working')

	def test_team_name(self):
		form = add_team({
			'teamName' : 'The Homies'
			})
		self.assertTrue(form.is_valid(), 'Form for team name is not valid')
		self.assertEqual(form.__dict__['data']['teamName'], 'The Homies', 'Form for team name is not capturing correctly')
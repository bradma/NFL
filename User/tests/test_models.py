from django.test import TestCase

from Select.models import user

class modal_user_test_cases(TestCase):
	def setUp(self):
		user.objects.create(id=0, user_name='Tester', wins=2, loses=3, total_week_wins=3, team_name='My_Test')

	def test_User(self):
		get_user = user.objects.get(id=0)
		self.assertEquals(str(get_user.user_name), 'Tester', 'Attribute: user_name is not working')
		self.assertEquals(get_user.wins, 2, 'Attribute: wins is not working')
		self.assertEquals(get_user.loses, 3, 'Attribute: loses is not working correctly')
		self.assertEquals(get_user.total_week_wins, 3, 'Attribute: total_week_wins is not working correctly')
		self.assertEquals(str(get_user.team_name), 'My_Test', 'Attribute: team_name is not working correctly')
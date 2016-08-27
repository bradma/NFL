from django.contrib.auth.models import User, AnonymousUser

from Select.models import user, game_week, game_pick

#Not sure if this is a good idea .... Might deperieciate out

class create_mock_scenario:
    def __init__(self):
        self.user_auth = User.objects.create_user(
            username='tester',
            password='Happy'
        )


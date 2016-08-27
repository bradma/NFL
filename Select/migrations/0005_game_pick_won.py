# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Select', '0004_user_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_pick',
            name='won',
            field=models.CharField(default=b'P', max_length=1),
            preserve_default=True,
        ),
    ]

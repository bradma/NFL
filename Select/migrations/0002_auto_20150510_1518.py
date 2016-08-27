# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Select', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_week',
            name='away_score',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game_week',
            name='home_score',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=True,
        ),
    ]

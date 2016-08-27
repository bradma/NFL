# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Select', '0002_auto_20150510_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_week',
            name='away_score',
            field=models.IntegerField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='game_week',
            name='home_score',
            field=models.IntegerField(default=0, max_length=20, null=True),
        ),
    ]

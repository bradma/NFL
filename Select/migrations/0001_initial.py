# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game_pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pick', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='game_week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team', models.CharField(max_length=30)),
                ('away_team', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('week', models.IntegerField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=10)),
                ('wins', models.IntegerField(default=0, max_length=20)),
                ('loses', models.IntegerField(default=0, max_length=20)),
                ('total_week_wins', models.IntegerField(default=0, max_length=20)),
            ],
            options={
                'ordering': ['-total_week_wins'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game_pick',
            name='game_weeks',
            field=models.ForeignKey(to='Select.game_week'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game_pick',
            name='user',
            field=models.ForeignKey(to='Select.user'),
            preserve_default=True,
        ),
    ]

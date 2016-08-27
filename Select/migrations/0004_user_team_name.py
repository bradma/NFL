# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Select', '0003_auto_20150516_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team_name',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]

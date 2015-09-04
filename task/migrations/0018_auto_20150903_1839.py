# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_auto_20150903_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_ep',
            field=models.TimeField(default=datetime.datetime(2015, 9, 4, 18, 39, 14, 630692), verbose_name=b'time end planned'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_ep',
            field=models.DateField(default=datetime.datetime(2015, 9, 4, 18, 39, 14, 630656), verbose_name=b'date end planned'),
        ),
    ]

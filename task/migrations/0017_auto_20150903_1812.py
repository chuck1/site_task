# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_auto_20150624_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_sp',
            field=models.TimeField(default=django.utils.timezone.now, null=True, verbose_name=b'time start planned', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_ep',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 4, 18, 12, 59, 375741), verbose_name=b'date end planned'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_sp',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date start planned'),
        ),
    ]

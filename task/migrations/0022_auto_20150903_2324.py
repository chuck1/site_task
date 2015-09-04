# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0021_auto_20150903_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_e',
        ),
        migrations.AlterField(
            model_name='task',
            name='date_ep',
            field=models.DateField(default=task.models.default_end, null=True, verbose_name=b'date end planned', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_sp',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name=b'date start planned', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_ep',
            field=models.TimeField(default=task.models.default_end, null=True, verbose_name=b'time end planned', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_auto_20150903_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_ep',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date end planned'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_ep',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'time end planned'),
        ),
    ]

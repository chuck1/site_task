# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0019_auto_20150903_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_ep',
            field=models.DateField(default=task.models.default_end, verbose_name=b'date end planned'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_ep',
            field=models.TimeField(default=task.models.default_end, verbose_name=b'time end planned'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0026_auto_20150904_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskdateoperation',
            old_name='date',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='tasktimeoperation',
            old_name='time',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_ea',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_ep',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_sa',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time_ea',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time_ep',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time_sa',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time_sp',
        ),
    ]

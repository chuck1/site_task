# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0022_auto_20150903_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='task',
            name='parent',
        ),
    ]

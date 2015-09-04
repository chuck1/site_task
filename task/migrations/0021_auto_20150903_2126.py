# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0020_auto_20150903_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_ea',
            field=models.TimeField(null=True, verbose_name=b'time end actual', blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='time_sa',
            field=models.TimeField(null=True, verbose_name=b'time start actual', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_ea',
            field=models.DateField(null=True, verbose_name=b'date end actual', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_sa',
            field=models.DateField(null=True, verbose_name=b'date start actual', blank=True),
        ),
    ]

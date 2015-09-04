# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0023_auto_20150903_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('op', models.IntegerField(choices=[(0, b'set start planned'), (1, b'set start actual'), (2, b'set end planned'), (3, b'set end actual')])),
            ],
        ),
    ]

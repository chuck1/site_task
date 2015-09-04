# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0024_taskoperation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDateOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('op', models.IntegerField(choices=[(0, b'set start planned'), (1, b'set start actual'), (2, b'set end planned'), (3, b'set end actual')])),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='TaskOperation',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_sp',
        ),
        migrations.AddField(
            model_name='taskdateoperation',
            name='task',
            field=models.ForeignKey(to='task.Task'),
        ),
    ]

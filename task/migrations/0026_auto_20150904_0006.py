# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0025_auto_20150903_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('op_code', models.IntegerField(choices=[(0, b'set start planned'), (1, b'set start actual'), (2, b'set end planned'), (3, b'set end actual')])),
            ],
        ),
        migrations.RemoveField(
            model_name='taskdateoperation',
            name='created',
        ),
        migrations.RemoveField(
            model_name='taskdateoperation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='taskdateoperation',
            name='op',
        ),
        migrations.RemoveField(
            model_name='taskdateoperation',
            name='task',
        ),
        migrations.CreateModel(
            name='TaskTimeOperation',
            fields=[
                ('taskoperation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='task.TaskOperation')),
                ('time', models.TimeField()),
            ],
            bases=('task.taskoperation',),
        ),
        migrations.AddField(
            model_name='taskoperation',
            name='task',
            field=models.ForeignKey(to='task.Task'),
        ),
        migrations.AddField(
            model_name='taskdateoperation',
            name='taskoperation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='task.TaskOperation'),
            preserve_default=False,
        ),
    ]

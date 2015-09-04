from django.db import models

# Create your models here.

import django.utils

import datetime
#import pytz

def default_end():
    return django.utils.timezone.now() + datetime.timedelta(days=1)

class TaskOperation(models.Model):
    OP_SET_STR_PLAN = 0
    OP_SET_STR_ACTU = 1
    OP_SET_END_PLAN = 2
    OP_SET_END_ACTU = 3

    op_choices = (
            (OP_SET_STR_PLAN, 'set start planned'),
            (OP_SET_STR_ACTU, 'set start actual'),
            (OP_SET_END_PLAN, 'set end planned'),
            (OP_SET_END_ACTU, 'set end actual'),
            )
    

    created = models.DateTimeField(auto_now_add = True)

    # fields

    op_code = models.IntegerField(choices=op_choices)
    
    task = models.ForeignKey('Task')

class TaskDateOperation(TaskOperation):
    value = models.DateField()

class TaskTimeOperation(TaskOperation):
    value = models.TimeField()

class Task(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField(blank=True)

    def set_date_or_time(self, op_class, v, op_code):
        if v is None:
            return
        op = op_class()
        op.op_code = op_code
        op.task = self
        op.value = v
        op.save()

    def set_date(self, d, op_code):
        self.set_date_or_time(TaskDateOperation, d, op_code)

    def set_time(self, d, op_code):
        self.set_date_or_time(TaskTimeOperation, d, op_code)



    def get_operation_value(self, op_class, op_code):
        ops = op_class.objects.filter(task=self, op_code=op_code).order_by('created')
        if ops:
            return ops[0].value
        return None

    def get_date_operation_value(self, op_code):
        return self.get_operation_value(TaskDateOperation, op_code)

    def get_time_operation_value(self, op_code):
        return self.get_operation_value(TaskTimeOperation, op_code)

    @property
    def date_sp(self):
        return self.get_date_operation_value(TaskOperation.OP_SET_STR_PLAN)

    @property
    def date_ep(self):
        return self.get_date_operation_value(TaskOperation.OP_SET_END_PLAN)

    @property
    def date_sa(self):
        return self.get_date_operation_value(TaskOperation.OP_SET_STR_ACTU)

    @property
    def date_ea(self):
        return self.get_date_operation_value(TaskOperation.OP_SET_END_ACTU)

    @property
    def time_sp(self):
        return self.get_time_operation_value(TaskOperation.OP_SET_STR_PLAN)

    @property
    def time_ep(self):
        return self.get_time_operation_value(TaskOperation.OP_SET_END_PLAN)

    @property
    def time_sa(self):
        return self.get_time_operation_value(TaskOperation.OP_SET_STR_ACTU)

    @property
    def time_ea(self):
        return self.get_time_operation_value(TaskOperation.OP_SET_END_ACTU)

    
    def __unicode__(self):
        return self.title




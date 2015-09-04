import django.utils
import django.forms

import datetime

class task_add(django.forms.Form):
    def __init__(self, *args, **kwargs):
        super(task_add, self).__init__(*args, **kwargs)
       
        fields = [
                ('sp','start planned'),
                ('ep','end planned'),
                ('sa','start actual'),
                ('ea','end actual'),
                ]
        
        field_types = [
                (django.forms.DateField, 'date'),
                (django.forms.TimeField, 'time'),
                ]

        for clas, s in field_types:
            for post, label in fields:
                name = s+'_'+post
                print "field: "+name
                f = clas(
                        label = s+' '+label,
                        required = False,
                        )
                self.fields[name] = f

        self.field_list = [
                (self.fields['date_sp'], self.fields['time_sp']),
                (self.fields['date_ep'], self.fields['time_ep']),
                (self.fields['date_sa'], self.fields['time_sa']),
                (self.fields['date_ea'], self.fields['time_ea']),
                ]
        """
        self.field_list = [
                ('date_sp', 'time_sp'),
                ('date_ep', 'time_ep'),
                ('date_sa', 'time_sa'),
                ('date_ea', 'time_ea'),
                ]
        """
    title = django.forms.CharField(max_length=256)
    #desc = django.forms.TextField(blank=True)

    #date_e  = django.forms.DateTimeField(
    #        'date entered', auto_now_add = True)

    # repetition
    repeat = django.forms.BooleanField(required=False,)
    
    repeat_mon = django.forms.BooleanField(required=False,)
    repeat_tue = django.forms.BooleanField(required=False,)
    repeat_wed = django.forms.BooleanField(required=False,)
    repeat_thu = django.forms.BooleanField(required=False,)
    repeat_fri = django.forms.BooleanField(required=False,)
    repeat_sat = django.forms.BooleanField(required=False,)
    repeat_sun = django.forms.BooleanField(required=False,)
    
    choices = [
            ('never','never'),
            ('date','date'),
            ('occurances','occurances'),
            ]

    repeat_end_condition = django.forms.ChoiceField(choices=choices, required=False)







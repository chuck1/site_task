from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
import django.db.models
import django.views.generic
import django.utils.timezone

# Create your views here.

import math
import datetime
import pytz

import task.models
import task.forms

def task_sorter(x,y):
    if x[0].date_ea and y[0].date_ea:
        return cmp(x[0].date_ea, y[0].date_ea)
    elif x[0].date_ea:
        return -1;
    elif y[0].date_ea:
        return 1;
    
    if x[0].date_ep:
        if y[0].date_ep:
            return cmp(x[0].date_ep, y[0].date_ep)

    return 0

def qry_task_active():
    tasks = list(sorted(gen_tasks(), task_sorter))
    #tasks = filter(lambda t: t[0].date_ea is None, tasks)
    return tasks

def get_datetime(d,t):
    dt = None

    if d and t:
        dt = datetime.datetime.combine(d, t)
        dt = dt.replace(tzinfo = django.utils.timezone.get_default_timezone())
        #dt = datetime.datetime.combine(d, t)
    
    return dt

def process_datetime_fields(d,t,tz):
    
    #tz = django.utils.timezone.get_default_timezone()

    #if t_sp:
    #    t_sp.tzinfo = django.utils.timezone.get_default_timezone()
    
    if t:
        t.replace(tzinfo = django.utils.timezone.get_default_timezone())
        pass

    dt = get_datetime(d,t)

    d_str = ""
    t_str = ""

    if dt:
        d_str = dt.astimezone(tz).strftime("%Y-%m-%d")
        t_str = dt.astimezone(tz).strftime("%H:%M:%S")
        #d_str = dt.strftime("%Y-%m-%d")
        #t_str = dt.strftime("%H:%M:%S")
    else:
        if d:
            d_str = d.strftime("%Y-%m-%d")

    return dt, d_str, t_str

def timedelta_str(td):
    if td is None:
        return ""

    MS = int(td.total_seconds() * 10**6)
    
    d = MS / (60*60*24*10**6)
   
    MS = MS % (60*60*24*10**6)
    
    h = MS / (60*60*10**6)
   
    MS = MS % (60*60*10**6)

    m = MS / (60*10**6)
   
    MS = MS % (60*10**6)

    s = MS / (10**6)
   
    MS = MS % (10**6)
 
    #return "{}:{:02}:{:02}:{:02}:{:06}".format(d,h,m,s,MS)
    return "{}:{:02}:{:02}:{:02}".format(d,h,m,s)

def html_class_start_planned(t):

    dt = get_datetime(t.date_sp, t.time_sp)
    
    if not t.date_sa:
    
        if dt:
            # date and time
            if dt < django.utils.timezone.now():
                return "task_list_warn"
        elif t.date_sp:
            # date only
            if t.date_sp < django.utils.timezone.now().date():
                return "task_list_warn"
    
    return ""

def html_class_dur_actual(dp, da):

    if da:
        if dp:
            if da > dp:
                return "task_list_warn"
            else:
                return "task_list_good"
    
    return ""


def gen_tasks():

    tz = pytz.timezone('America/Los_Angeles')
    
    for t in task.models.Task.objects.all():

        dt_sp, d_sp_str, t_sp_str = process_datetime_fields(t.date_sp, t.time_sp, tz)
        dt_ep, d_ep_str, t_ep_str = process_datetime_fields(t.date_ep, t.time_ep, tz)
        dt_sa, d_sa_str, t_sa_str = process_datetime_fields(t.date_sa, t.time_sa, tz)
        dt_ea, d_ea_str, t_ea_str = process_datetime_fields(t.date_ea, t.time_ea, tz)

        dp = None
        da = None

        if dt_sa:
            if dt_ea:
                da = dt_ea - dt_sa
            else:
                da = django.utils.timezone.now() - dt_sa
        elif t.date_sa:
            if d_ea:
                da = t.date_ea - t.date_sa
            else:
                da = django.utils.timezone.now().date() - t.date_sa


        
        if dt_ep and dt_sp:
            dp = dt_ep - dt_sp
        elif t.date_ep and t.date_sp:
            dp = t.date_ep - t.date_sp
        
        dp_str = timedelta_str(dp)
        da_str = timedelta_str(da)
        
        yield (
                t,
                {'d': d_sp_str, 't': t_sp_str, 'class': html_class_start_planned(t)},
                {'d': d_ep_str, 't': t_ep_str, 'class':''},
                {'d': d_sa_str, 't': t_sa_str, 'class':''},
                {'d': d_ea_str, 't': t_ea_str, 'class':''},
                {'str': dp_str, 'class':''},
                {'str': da_str, 'class': html_class_dur_actual(dp, da)})

class Day:
    def __init__(self, date, tasks):
        self.date = date

        if self.date == datetime.date.today():
            self.html_class = "today"

        self.tasks = []
        
        print "Day", self.date

        for task,_,_,_,_,_,_ in tasks:
            if task.date_ep.date() == self.date:
                print " ", task.date_ep.date()
                self.tasks.append(task)

class Calendar:
    def __init__(self, tasks):
        t = datetime.date.today()
        m = t.month
        d = datetime.date(t.year, m, 1)
        
        w = 0
        self.weeks = [[""]*7]
        
        while d.month == m:
            wd = d.weekday()
            self.weeks[w][wd] = Day(d, tasks)
            
            d = d + datetime.timedelta(days=1)
            
            if wd == 6:
                if d.month != m:
                    break
                
                self.weeks.append([""]*7)
                w = w + 1


def calendar(request):
    tasks = qry_task_active()
    
    context = {'cal': Calendar(tasks)}
    
    return render(request, 'task/calendar.html', context)

def lst(request):
    tasks = qry_task_active()

    context = {'tasks': tasks}

    return render(request, 'task/list.html', context)

def start_now(request, task_id):
    
    t = get_object_or_404(task.models.Task, pk=task_id)
    
    t.date_sa = django.utils.timezone.now()

    if t.time_sp:
        t.time_sa = django.utils.timezone.now()

    t.save()
    
    return HttpResponseRedirect(reverse('task:lst'))

def end_now(request, task_id):
    
    t = get_object_or_404(task.models.Task, pk=task_id)
    
    t.date_ea = django.utils.timezone.now()
    
    if t.time_sp:
        t.time_ea = django.utils.timezone.now()

    t.save()
    
    return HttpResponseRedirect(reverse('task:lst'))

def index(request):
    return render(request, 'task/index.html', {})
    
def form_task_add(request):
    
    if request.method == 'POST':
        form = task.forms.task_add(request.POST)
        
        if form.is_valid():
            t = task.models.Task()
            
            t.title = form.cleaned_data['title']
            
            t.save()

            t.set_date(
                    form.cleaned_data['date_sp'],
                    task.models.TaskOperation.OP_SET_STR_PLAN)
            t.set_date(
                    form.cleaned_data['date_ep'],
                    task.models.TaskOperation.OP_SET_END_PLAN)
            t.set_date(
                    form.cleaned_data['date_sa'],
                    task.models.TaskOperation.OP_SET_STR_ACTU)
            t.set_date(
                    form.cleaned_data['date_ea'],
                    task.models.TaskOperation.OP_SET_END_ACTU)

            t.set_time(
                    form.cleaned_data['time_sp'],
                    task.models.TaskOperation.OP_SET_STR_PLAN)
            t.set_time(
                    form.cleaned_data['time_ep'],
                    task.models.TaskOperation.OP_SET_END_PLAN)
            t.set_time(
                    form.cleaned_data['time_sa'],
                    task.models.TaskOperation.OP_SET_STR_ACTU)
            t.set_time(
                    form.cleaned_data['time_ea'],
                    task.models.TaskOperation.OP_SET_END_ACTU)

            return HttpResponseRedirect(reverse('task:lst'))
        else:
            print "invalid"
    else:
        form = task.forms.task_add()

    return render(request, 'task/form_task_add.html', {'form':form})


def task_detail(request, task_id):

    t = get_object_or_404(task.models.Task, pk=task_id)

    return render(request, 'task/task_detail.html', {'task': t})



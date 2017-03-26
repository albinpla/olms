from user_login.forms import leave_app_form
from django.views import View
from django.shortcuts import render,HttpResponse
from user_login.forms import UserForm,UserprofileForm
from .models import Employee,leave_statistics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

class leave_apply(View):
    # set to false initially as request is not submitted
    applied = False
    template=""
    def get(self,request):
        applied = False
        try:
            profile = Employee.objects.get(user=request.user)
        except TypeError:
            return HttpResponse('No user logged in:-(:-(<br>Please <a href="/user/login/">login</a>')
        if profile.user.is_authenticated:
            template="user_login/applyleave.html"
            leave_stat = leave_statistics.objects.get(user=profile.user)
            return render(request,template,{'profile':profile,'leave_app_form': leave_app_form, 'applied': applied,'leave':leave_stat} )

    def post(self,request):
        # If it's a HTTP POST, we're interested in processing form data.
        # Attempt to grab information from the raw form information.
        leave_form = leave_app_form(data=request.POST)
        # retrieve user
        profile = Employee.objects.get(user=request.user)
        # If the two forms are valid...
        if leave_form.is_valid():
            # leave_form not saved
            leave_app = leave_form.save(commit=False)
            # setting user of leaveform
            leave_app.user=profile.user
            #returning the leave_history of that user to leave_stat
            leave_stat=leave_statistics.objects.get(user=profile.user)
            # print(leave_app.user.get_username())
            # print(leave_stat.user.get_username())
            # print(leave_app.half_day)
            # print(leave_app.leavetype)
            check_leave(leave_app=leave_app,leave_stat=leave_stat)
            print(leave_stat.casual)
            leave_app.save()
            return HttpResponse('Leave Application Successful!!')

def check_leave(leave_app,leave_stat):
    flag=False
    leave={
        'cl','hp'
        }
    if leave_app.leavetype == 'cl':
        if leave_app.half_day < leave_stat.casual:
            leave_stat.casual-= leave_app.half_day
            flag=True

    elif leave_app.leavetype == 'hp':
        if leave_app.half_day < leave_stat.casual:
            leave_stat.half_paid-= leave_app.half_day
            flag=True
    leave_stat.save()
    if flag==False:
        return HttpResponse('Incorrect leave Application<br><a href="/user/apply_leave/">Redo</a>')     
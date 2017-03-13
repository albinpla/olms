from user_login.forms import leave_app_form
from django.views import View
from django.shortcuts import render
from user_login.forms import UserForm,UserprofileForm
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class leave_apply(View):
	# set to false initially as request is not submitted
	applied = False
	template=""
	# @login_required
	def get(self,request):
		applied = False
		profile = Employee.objects.get(user=request.user)
		template="user_login/applyleave.html"
		return render(request,template,{'profile':profile,'leave_app_form': leave_app_form, 'applied': applied} )
	# @login_required	
	# def post(self,request):
	# 	pass


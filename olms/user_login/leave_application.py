from user_login.forms import leave_app_form
from django.views import View
from django.shortcuts import render

class leave_apply(View):
	# set to false initially as request is not submitted
	applied = False
	template=""
	def get(self,request):
		applied = False
		template="user_login/applyleave.html"
		return render(request,template,{'leave_app_form': leave_app_form, 'applied': applied} )

	def post(self,request):
		pass


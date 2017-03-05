from django.shortcuts import render

# Create your views here.
def home(request):
	context={}
	template='user_login/home.html'
	return render(request,template,context)
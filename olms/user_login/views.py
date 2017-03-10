from django.shortcuts import render
from .forms import loginform
# Create your views here.
def home(request):
	form=loginform
	context={"form":form}
	template='user_login/home.html'
	return render(request,template,context)
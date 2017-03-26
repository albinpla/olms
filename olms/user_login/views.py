from django.shortcuts import render,redirect
from .forms import loginform
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Employee,leave_history
from .models import Employee
# Create your views here.

class user_login(View):
        def get(self,request):
                form=loginform
                context={"form":form}
                template='user_login/login.html'
                return render(request,template,context)




        def post(self,request):
                # If the request is a HTTP POST, try to pull out the relevant information.
                # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception

                username = request.POST.get('username')
                password = request.POST.get('password')
                # Use Django's machinery to attempt to see if the username/password
                # combination is valid - a User object is returned if it is.
                user = authenticate(username=username, password=password)
                # If we have a User object, the details are correct.
                # If None (Python's way of representing the absence of a value), no user
                # with matching credentials was found.
                if user:
                        # Is the account active? It could have been disabled.
                        if user.is_active:
                                # If the account is valid and active, we can log the user in.
                                # We'll send the user back to the homepage.
                                login(request, user)
                                print(request.POST['username'],request.POST['password'],user.username)
                                return redirect('/user/hello/')
                        else:
                                # An inactive account was used - no logging in!
                                return HttpResponse("Your account is disabled.")
                else:
                        # Bad login details were provided. So we can't log the user in.
                        print("Invalid login details: {0}, {1}".format(username, password))
                        return HttpResponse("Invalid login details supplied.")

@login_required
def user_logout(request):
        # Since we know the user is logged in, we can now just log them out.
        logout(request)
        # Take the user back to the homepage.
        return HttpResponseRedirect('/user/login/')

def home(request):
        context={}
        template='user_login/welcome.html'
        return render(request,template,context)

@login_required
def userpage(request):
        profile = Employee.objects.get(user=request.user)
        template='user_login/hi.html'
        print(request.user.get_username())
        return render(request,template,{'profile':profile})    
          
class leave_cancel(View):
        def get(self,request):
                template = 'user_login/leave_cancel.html'
                profile = Employee.objects.get(user=request.user)
                return render(request, template, {'profile': profile})

        def post(self,request):
                template='user_login/leave_cancel.html'
                profile = Employee.objects.get(user=request.user)
                return render(request,template,{'profile':profile})


class leave_history(View):
        def get(self,request):
                template= 'user_login/leave_history.html'
                profile = Employee.objects.get(user=request.user)
                return render(request, template, {'profile': profile})
        def post(self,request):
                template='user_login/leave_history.html'
                profile = Employee.objects.get(user=request.user)
                history = leave_history.objects.get(user=request.user)
                if history:
                        print ("sucesss")

                else:
                        print ("error")
                return render(request,template,{'profile':profile})

class check_status(View):
        def get(self,request):
                template = 'user_login/check_status.html'
                profile = Employee.objects.get(user=request.user)
                return render(request, template, {'profile': profile})

        def post(self,request):
                template='user_login/check_status.html'
                profile = Employee.objects.get(user=request.user)
                return render(request,template,{'profile':profile})

class statistics(View):
        def get(self,request):
                template = 'user_login/statistics.html'
                profile = Employee.objects.get(user=request.user)
                return render(request, template, {'profile': profile})

        def post(self,request):
                template='user_login/statistics.html'
                profile = Employee.objects.get(user=request.user)
                return render(request,template,{'profile':profile})

class profile(View):
        def get(self,request):
                template = 'user_login/profile.html'
                profile = Employee.objects.get(user=request.user)
                return render(request, template, {'profile': profile})

        def post(self,request):
                template='user_login/profile.html'
                profile = Employee.objects.get(user=request.user)
                return render(request,template,{'profile':profile})







from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm

def register_new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Now you can log in")
    elif request.method == "GET":
        form = UserCreationForm()
    return render(request, 'login_screen/register_new_user.html', context={'form':form})

def loginview(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return render(request, 'login_screen/login.html', context={'form':form})
    else:
        form = LoginForm(request)
    request.session.set_test_cookie()
    return render(request, 'login_screen/login.html', context={'form':form})


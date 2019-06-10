from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import LoginForm


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
            )
            auth.login(request, user)
            return redirect('home')
        
    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse('아이디 혹은 패스워드가 잘못 입력되었습니다.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})



def logout(request):
    auth.logout(request)
    return redirect('home')
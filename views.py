from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login
# function_based views
def register(request):
    if request.method == 'GET':
        return render(request, 'auth_app/register.html')
    else:
        first_pasword = request.POST['password']
        second_password = request.POST['password_2']
        if first_pasword == second_password:
            try:
                user = User.objects.create_user(username = request.POST['username'],email = request.POST['email'], password = request.POST['password'])
                user.save()
                response = redirect('/account/')
                return response
            except IntegrityError:
                return render(request, 'auth_app/register.html')
        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})
def login(request):
    if request.method == 'POST':
        username_1 = request.POST['username']
        password_1 = request.POST['password']
        user = authenticate(request, username=username_1, password=password_1)
        if user != None:
            user_login(request, user)
            return render(request,'auth_app/login.html',{'my_user':user})
        else:
            error = "the username or password is invalid"
            return render(request,'auth_app/login.html',{'error':error})
    else:
        if request.user.is_authenticated:
            response = redirect('/account/')
            return response
        else:
           return render(request,'auth_app/login.html') 

def home(request):
    if request.user.is_authenticated and request.POST:
        logout(request)
        return render(request, 'auth_app/home.html') 
    else:
        return render(request, 'auth_app/home.html')
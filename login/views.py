from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def signup(request):
    
    if request.method == "GET":
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                #registrando usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("profesores")
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password does not match'
        })
           
    
def profesores(request):
    return render(request, 'profesores.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })

        return render(request, 'signin.html', {
            'form': AuthenticationForm,

        })

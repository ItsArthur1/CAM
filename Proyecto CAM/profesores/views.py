from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                return HttpResponse("User created Successfully")
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password does not match'
        })
           
    
from django.contrib.auth.models import User, auth
from django.contrib.postgres.search import *
from django.shortcuts import render, redirect
from . import afterLogin
from .models import Profile
from .forms import loginForm, signUpForm
        
def index(request):
    return render(request, 'index.html')

def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            date_of_birth=request.POST['date_of_birth']
            password = request.POST['password1']
            
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            profile = Profile(user=user, name=name, date_of_birth=date_of_birth)
            profile.save()
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('/home')
        
        else:
            return render(request, 'signUp.html', {'form': form})

    form = signUpForm()
    return render(request, 'signUp.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                print(user)
                return redirect('/home')

    form = loginForm()
    return render(request, 'login.html', {'form': form})

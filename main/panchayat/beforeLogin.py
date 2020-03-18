from django.contrib.auth.models import User, auth
from django.contrib.postgres.search import *
from django.shortcuts import render, redirect
from . import afterLogin
from .models import Profile

        
def index(request):
    return render(request, 'index.html')
    
def login(request):
    return render(request, 'login.html')

def signUp(request):
    return render(request,'signUp.html')

def loginUser(request):
    try :
        username=request.POST['username']
        password=request.POST['password']
    except :
        return render(request, 'login.html')
    
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/home')

    else:

        return render(request,'login.html',{"message":"invalid password"})

def createUser(request):
    try:
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    except :
        return render(request,'SignUp.html')

    if (password1 == password2):
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            return render(request,'signUp.html',{"message":"User already exists"})
        else:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            profile = Profile(user=user, name=name)
            profile.save()
            user = auth.authenticate(username=username, password=password1)

            if user is not None:
                auth.login(request,user)
                return redirect('/home')
            
    else:
        return render(request, 'signUp.html', {"message": "Passwords Do Not Match"})

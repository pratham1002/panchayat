from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def home(request):
    currentUser=request.user

    return render(request, 'home.html', {"userdata": currentUser})

def logout(request):
    auth.logout(request)
    return redirect('/')
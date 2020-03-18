from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def default(request):
    return render(request, '404.html')

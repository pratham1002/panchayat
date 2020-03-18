from django.urls import path
from . import views, beforeLogin, afterLogin

urlpatterns = [
    path('', beforeLogin.index),
    path('login', beforeLogin.login),
    path('signUp', beforeLogin.signUp),
    path('createUser', beforeLogin.createUser),
    path('loginUser', beforeLogin.loginUser),
    path('home', afterLogin.home),
    path('logout', afterLogin.logout),
]
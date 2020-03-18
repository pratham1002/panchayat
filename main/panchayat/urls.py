from django.urls import path
from . import views, beforeLogin, afterLogin

urlpatterns = [
    path('', views.index),
]
from django.urls import path
from . import views, beforeLogin, afterLogin

urlpatterns = [
    path('', beforeLogin.index),
    path('login', beforeLogin.login),
    path('signUp', beforeLogin.signUp),
    path('home', afterLogin.home),
    path('logout', afterLogin.logout),
    path('following', afterLogin.showFollowing),
    path('followers', afterLogin.showFollowers),
    path('allUsers', afterLogin.showAllUsers),
    path('followPerson', afterLogin.followPerson),
    path('unfollowPerson', afterLogin.unfollowPerson),
    path('profile', afterLogin.profile),
    path('newPost', afterLogin.newPost),
    path('feed', afterLogin.feed),
    path('editProfile', afterLogin.editProfile),
]
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=256)
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')
    date_of_birth = models.DateField()
    
class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    numberOfComments = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    uploader = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

class Follower(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='current_user_follower')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='is_follower')

class Following(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='current_user_following')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='is_following')
    
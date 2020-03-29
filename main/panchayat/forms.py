from django import forms
from django.contrib.auth.models import User
from django.contrib.postgres.search import *
import datetime
from .models import Profile

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)

class signUpForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    date_of_birth = forms.DateField(initial=datetime.date.today)
    email = forms.CharField(label='email', max_length=100)
    password1 = forms.CharField(label='password1', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('passwords do not match')

        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise forms.ValidationError('email/username not unique')

class profileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'profile_picture','date_of_birth']
    

    
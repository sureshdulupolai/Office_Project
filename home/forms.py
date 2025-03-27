from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userSignupPage(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

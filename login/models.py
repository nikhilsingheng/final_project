from django import forms
from django.contrib.auth import login
# from django.contrib.auth.models import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db import  models
# User = get_user_model()


class UsersignForm(models.Model):
	email = models.EmailField()
	Password = models.CharField(max_length=20)
	repeat_Password = models.CharField(max_length=20)
	# class Meta:
	# 	model = login
	# 	fields = ['email',  'password', 'repeat_password']

# class UserloginForm(models.Model):
# 	email = models.EmailField()
#
# 	password = models.CharField(max_length = 20)
	
	# class Meta:
	# 	model = login
	# 	fields = ['email', 'password']


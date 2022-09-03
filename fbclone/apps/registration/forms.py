from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class NewUserForm(UserCreationForm):
	#firstname=forms.TextInput()
	#listname=forms.TextInput()
	#email=forms.EmailInput()
	class Meta:
		model=User
		fields=['id','username','first_name','last_name','email']

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['id','photo','title','discription']
		labels={'photo':''}
		
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Post, Template, Profile


class UserCreationForm2(UserCreationForm):
	
	class Meta:
		model = User
		fields = [		
		'username',
		'password1',
		'password2',
		'email',
		'first_name',
		'last_name'		
		]



class EditProfleForm(UserChangeForm):
	
	class Meta:
		model = User
		fields = {
		'email',
		'first_name',
		'last_name',
		'password'
		}

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = {
		'title',
		'text',
		}

class TemplateForm(forms.ModelForm):

	class Meta:
		model = Template
		fields = {
		'nickname',
		'colour',
		}

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = {
		'City',
		'School',
		'College',
		'About_me',
		}
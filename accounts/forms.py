from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create the form class.
class SettingsForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'
		exclude = ['user']

class UserForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'

class MeetingForm(ModelForm):
	class Meta:
		model = Meeting
		fields = '__all__'

class DealForm(ModelForm):
	class Meta:
		model = Deal
		fields = '__all__'

class RegisterUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
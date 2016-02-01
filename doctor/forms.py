from django.contrib.auth.models import User
from django.forms import ModelForm

class DoctorRegistrationForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name','last_name', 'email', 'password')
class UserLoginForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CoreUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CoreUser
        fields = ['name','username','email','profilephoto','birthdate']

from django import forms
from django.contrib.auth.models import User
from . models import user

#class AdminSignupForm(forms.ModelForm):
#   class Meta:
#       model = User
#       fields = ['email','password']
#       widgets = {
#           'password':forms.PasswordInput()
#       }

class UserForm(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"
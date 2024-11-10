from dataclasses import field, fields
from operator import mod
from django import forms
from user.models import *

# class AdminForm(forms.ModelForm):
#     class Meta:
#         model=Admin
#         fields="__all__"

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields="__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"
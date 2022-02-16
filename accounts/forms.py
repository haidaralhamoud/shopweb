from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2',]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('user','photo')



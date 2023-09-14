from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Create a username'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your First name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Last name'}), required=False)  
    email_address = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'name@example.com', 'class':"form-control"}), required=True)
    create_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Create a password'}), required=True, min_length="6")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}), required=True, min_length="6")

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write your username', 'class':"form-control"}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', 'class':"form-control"}), required=True)
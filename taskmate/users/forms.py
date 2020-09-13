from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.Textarea()
    last_name = forms.Textarea()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
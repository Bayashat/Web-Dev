from django.contrib.auth.forms import AuthenticationForm

from django import forms

from .models import CustomUser

# Tell the admin to use these forms by subclassing UserAdmin in users/admin.py:
class CustomUserLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': "exampleInputEmail1",
        'placeholder': 'Your Email'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'id' : "exampleInputPassword1",
        'placeholder' : 'Your Password'
    }))

    class Meta:
        model = CustomUser
        fields = ("email", "password")


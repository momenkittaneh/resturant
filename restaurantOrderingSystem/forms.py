from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ('tableno',)


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))

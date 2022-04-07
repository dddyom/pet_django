from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm, UserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Not selected'

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("length more than 200!")

        return title


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(
        label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(
        label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='password repeat', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

class ContactForm(forms.Form):
    username = forms.CharField(
        label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(
        label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='content', widget=forms.PasswordInput(
        attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

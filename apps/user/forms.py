from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
import uuid
from datetime import timedelta
from .tasks import send_verification_email


class RegisterForm(UserCreationForm):

    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class':'login-input' }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя', 'class':'login-input' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите фамилию', 'class':'login-input' }))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'login-input' }), required=False)
    email= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите электронную почту','class':'login-input', 'type':'email'}))
    password1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите пароль', 'class':'login-input', 'type':'password'}))
    password2= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Потвердите пароль', 'class':'login-input', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

   
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=True)
        # user = super(UserRegistrationForm, self).save(commit=True)
        # expiration = timezone.now() + timedelta(hours=48)
        # record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        send_verification_email.delay(user.id)
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'login-input'})),     
    passvord = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'login-input'})),     


class UserProfileForm(UserChangeForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class':'login-input' }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя', 'class':'login-input' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите фамилию', 'class':'login-input' }))
    email= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите электронную почту','class':'login-input', 'type':'email','readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'login-input' }), required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image']
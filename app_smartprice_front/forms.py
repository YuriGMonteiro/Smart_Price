from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import forms as auth_form
from django.contrib.auth import get_user_model

User = get_user_model()


class UserChangeForm(auth_form.UserChangeForm):
    class Meta(auth_form.UserChangeForm.Meta):
        model = User


class UserCreationForm(auth_form.UserCreationForm):
    class Meta(auth_form.UserCreationForm.Meta):
        model = User

    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','token','password1','password2')
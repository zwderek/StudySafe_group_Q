from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
        

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        
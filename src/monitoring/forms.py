from django import forms
from .models import User


class UserLoginForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = User
        exclude = ("cpf", "userType")

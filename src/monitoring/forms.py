from django import forms
from .models import User


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ("cpf", "userType")

        labels = {
            'username': 'Nome do usuário',
            'password': 'Senha',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Digite o nome do usuário'}),
            'password': forms.TextInput(attrs={'placeholder': 'Digite sua senha'}),
        }

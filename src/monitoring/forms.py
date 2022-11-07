from django import forms
from django.contrib.auth import get_user_model


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

        labels = {
            'username': 'Nome do usuário',
            'password': 'Senha',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Digite o nome do usuário'}),
            'password': forms.TextInput(attrs={'placeholder': 'Digite sua senha'}),
        }

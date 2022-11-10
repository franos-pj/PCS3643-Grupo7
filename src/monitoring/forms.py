from .models import Route, Flight
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
            'password': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        }


# creating a form
class RouteForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Route

        # specify fields to be used
        fields = "__all__"

        labels = {
            "flightCode": "Código",
            "airline": "Companhia",
            "departureAirport": "Origem",
            "arrivalAirport": "Destino",
            "scheduledTime": "Horário Previsto",
        }

        widgets = {
            "flightCode": forms.TextInput(
                attrs={"placeholder": "Digite um código de voo"}
            ),
            "airline": forms.TextInput(
                attrs={"placeholder": "Digite um companhia aérea"}
            ),
            "departureAirport": forms.TextInput(
                attrs={"placeholder": "Digite o aeroporto de origem"}
            ),
            "arrivalAirport": forms.TextInput(
                attrs={"placeholder": "Digite o aeroporto de destino"}
            ),
            "scheduledTime": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
        }


class FlightForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Flight

        # specify fields to be used
        fields = ["route", "scheduledDate"]

        labels = {
            "route": "Código",
            "scheduledDate": "Data Prevista",
        }

        widgets = {
            "route": forms.TextInput(
                attrs={
                    "placeholder": "Digite um código de voo",
                }
            ),
            "scheduledDate": forms.TimeInput(
                format=("%d-%m-%Y"),
                attrs={
                    "type": "date",
                    "placeholder": "Selecione uma data",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.fields["route"] = forms.ModelChoiceField(
            queryset=Route.objects.all(),
            empty_label="",
            label="Código de voo",
        )

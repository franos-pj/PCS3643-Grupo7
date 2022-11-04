from django import forms
from .models import Route
 
 
# creating a form
class RouteForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Route

 
        # specify fields to be used
        fields = "__all__"

        labels = {
            'flightCode': 'Código',
            'airline': 'Companhia',
            'departureAirport': 'Origem',
            'arrivalAirport': 'Destino',
            'scheduledTime': 'Horário Previsto'
        }
        
        widgets = {
            'flightCode': forms.TextInput(attrs={'placeholder': 'Digite um código de voo'}),
            'airline': forms.TextInput(attrs={'placeholder': 'Digite um companhia aérea'}),
            'departureAirport': forms.TextInput(attrs={'placeholder': 'Digite o aeroporto de origem'}),
            'arrivalAirport': forms.TextInput(attrs={'placeholder': 'Digite o aeroporto de destino'}),
            'scheduledTime': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
        }
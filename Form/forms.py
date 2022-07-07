from django import forms
from Form.models import Formulaire


class TaskFormulaire(forms.ModelForm):
    class Meta:
        model = Formulaire
        exclude = ['etat','date_destruction']
        widgets = {
            'date_début': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
            'date_de_demande': forms.DateInput(attrs={'type': 'date'})

        }

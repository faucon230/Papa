from django import forms
from Form.models import Formulaire


class TaskFormulaire(forms.ModelForm):
    class Meta:
        model = Formulaire
        exclude = ['etat','date_destruction']

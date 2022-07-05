from django import forms
from Form.models import Formulaire



class TaskFormulaire(forms.ModelForm):
    class Meta:
        model = Formulaire
        fields = '__all__'
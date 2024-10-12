from django import forms
from .models import Personaje
# Clase 26-09-2024
class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        # fields = ['alias', 'nombre_completo', 'aldea', 'clan', 'foto']
        fields = '__all__'
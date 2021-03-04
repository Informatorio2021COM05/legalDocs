from django import forms
from django.forms import ModelForm, DateInput
from django.forms.widgets import TimeInput
from .models import Documento, Turno


class DocumentoForm(ModelForm):
    descripción = forms.CharField(widget=forms.Textarea, max_length=300, required = False)
    
    class Meta:
        model = Documento
        fields = ('cliente', 'titulo', 'descripción', 'paginas')



class TurnoForm(ModelForm):
    fecha = forms.DateField(widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}), required=False)
    hora = forms.TimeField(widget=TimeInput(format= '%H:%M', attrs={'type': 'time'}), required=False)
    cliente = forms.IntegerField(required=False)
    escribano = forms.IntegerField(required=False)

    class Meta:
        model = Turno
        fields = '__all__'



class EditarTurnoForm(ModelForm):
    fecha = forms.DateField(widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    hora = forms.TimeField(widget=TimeInput(format= '%H:%M', attrs={'type': 'time'}))

    class Meta:
        model = Turno
        fields = ('fecha', 'hora',)
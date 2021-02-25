from django import forms
from django.forms import ModelForm, DateInput
from django.forms.widgets import TimeInput
from .models import Documento, Turno
from .validators import validate_file_extension


class DocumentoForm(ModelForm):
    título = forms.CharField(max_length=50)
    descripción = forms.CharField(max_length=300, required=False)
    número_de_páginas = forms.IntegerField()
    archivo = forms.FileField(required=False, validators=[validate_file_extension])

    class Meta:
        model = Documento
        fields = ('titulo', 'descripcion', 'paginas', 'archivo')



class TurnoForm(ModelForm):
    fecha = forms.DateField(widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}), required=False)
    hora = forms.TimeField(widget=TimeInput(format= '%H:%M', attrs={'type': 'time'}), required=False)
    class Meta:
        model = Turno
        fields = ('fecha',)
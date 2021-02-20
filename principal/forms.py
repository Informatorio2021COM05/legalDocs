from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class BasicSignupForm(forms.Form):
    usuario = forms.CharField(validators=[validators.MinLengthValidator(5),
        validators.MaxLengthValidator(30)])
    nombre = forms.CharField(validators=[
        validators.MaxLengthValidator(30)])
    apellido = forms.CharField(validators=[
        validators.MaxLengthValidator(30)])
    dni = forms.IntegerField(validators=[validators.MinValueValidator(1000000),
        validators.MaxValueValidator(100000000)])
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=30, widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(max_length=30, widget=forms.PasswordInput)


class ExtendSignupForm(BasicSignupForm):
    matrícula = forms.IntegerField()
    provincia = forms.CharField(validators=[
        validators.MaxLengthValidator(50)])
    ciudad = forms.CharField(validators=[
        validators.MaxLengthValidator(50)])
    calle = forms.CharField(validators=[
        validators.MaxLengthValidator(50)])
    altura = forms.IntegerField()
    piso = forms.IntegerField(validators=[
        validators.MinValueValidator(0)])
    número_de_puerta = forms.CharField(validators=[
        validators.MaxLengthValidator(5)])



from django.forms import ModelForm, fields
from .models import Cliente, Escribano


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class EscribanoForm(ModelForm):
    class Meta:
        model = Escribano
        fields = '__all__'
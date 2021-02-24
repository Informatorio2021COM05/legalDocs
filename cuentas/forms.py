from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.query_utils import Q
from .models import CustomUser, Escribano
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'dni', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('nombre', 'apellido', 'dni', 'email',)



class EscribanoCreationForm(UserCreationForm):
    opciones = ((1, 'Buenos Aires'), (2, 'Capital Federal'), (3, 'Catamarca'), (4, 'Chaco'),
        (5, 'Chubut'), (6, 'Córdoba'), (7, 'Corrientes'), (8, 'Entre Ríos'), (9, 'Formosa'),
        (10, 'Jujuy'), (11, 'La Pampa'), (12, 'La Rioja'), (13, 'Mendoza'), (14, 'Misiones'),
        (15, 'Neuquén'), (16, 'Río Negro'), (17, 'Salta'), (18, 'San Juan'), (19, 'San Luis'),
        (20, 'Santa Cruz'), (21, 'Santa Fe'), (22, 'Santiago del Estero'),
        (23, 'Tierra del Fuego'), (24, 'Tucumán'),
        )
    
    matricula = forms.IntegerField()
    provincia = forms.ChoiceField(choices=opciones)
    ciudad = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=50)
    altura = forms.IntegerField()
    piso = forms.IntegerField(required=False)
    numeroPuerta = forms.CharField(max_length=4, required=False)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'nombre', 'apellido', 'dni', 'email', 'matricula', 'provincia', 'ciudad',
            'calle', 'altura', 'piso', 'numeroPuerta',
            )
    
    def save(self):
        user = super(EscribanoCreationForm, self).save()
        user.is_escribano = True
        user.save()
        matricula = self.cleaned_data['matricula']
        provincia = self.cleaned_data['provincia']
        ciudad = self.cleaned_data['ciudad']
        calle = self.cleaned_data['calle']
        altura = self.cleaned_data['altura']
        piso = self.cleaned_data['piso']
        numeroPuerta = self.cleaned_data['numeroPuerta']

        user = Escribano.objects.create(
            customuser_ptr=user, matricula = matricula, provincia = provincia,
            ciudad = ciudad, calle = calle, altura = altura, piso= piso,
            numeroPuerta = numeroPuerta
            )
        return user

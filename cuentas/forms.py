from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
    matricula = forms.IntegerField()
    provincia = forms.CharField(max_length=50)
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

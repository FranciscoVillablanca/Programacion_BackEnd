from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'

    def clean_email(self):
        input_email = self.cleaned_data.get('email')
        if input_email.find('@') == -1:
            raise forms.ValidationError("El email debe contener un @")
        return input_email
    
    def clean_nombre(self):
        input_nombre = self.cleaned_data['nombre']
        if len(input_nombre) > 80:
            raise forms.ValidationError("El largo máximo para el nombre es 80 caracteres")
        return input_nombre
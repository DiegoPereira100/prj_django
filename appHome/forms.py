from django import forms
from appHome.models import Usuario

class FormUser(forms.ModelForm):
  class Meta:
    #modelo do formulario
    model = Usuario
    #campos do formulario
    fields = ('name', 'lastname')


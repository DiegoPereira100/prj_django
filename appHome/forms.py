from django import forms
from appHome.models import Usuario, Curso

class FormUser(forms.ModelForm):
  class Meta:
    #modelo do formulario
    model = Usuario
    #campos do formulario
    fields = ('name', 'lastname')

class FormCourse(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ('name', 'autor', 'duration', 'price')
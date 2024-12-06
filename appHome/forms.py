from django import forms
from appHome.models import Usuario, Curso, Login

class FormUser(forms.ModelForm):
  class Meta:
    #modelo do formulario
    model = Usuario
    #campos do formulario
    fields = ('name', 'lastname')

from django import forms
from appHome.models import Usuario, Curso, Login

class FormCourse(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('name', 'autor', 'duration', 'price', 'stock')  # Adiciona 'estoque' ao formulário


class FormLogin(forms.ModelForm):
  class Meta:
    model = Login
    fields = ('email', 'password')

    widgets = {
      'email': forms.TextInput(attrs={'class': 'form-control border border-sucess', 'type':'email'}),
      'password': forms.TextInput(attrs={'class': 'form-control border border-sucess', 'type':'password'})
    }


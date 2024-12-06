from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Usuario(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Curso(models.Model):
    name = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Aqui estamos adicionando o campo `stock` com valor padrão 0.

    def __str__(self):
        return self.name

class Venda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)  # Permite NULL
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.usuario} comprou {self.curso.name}"

class Login(models.Model):
    user = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=16)

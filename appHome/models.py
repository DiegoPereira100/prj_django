from django.db import models


class Usuario(models.Model):
  name = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Curso(models.Model):
  name = models.CharField(max_length=255)
  autor = models.CharField(max_length=255)
  duration = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)

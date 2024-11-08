from django.db import models


class Usuario(models.Model):
  name = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
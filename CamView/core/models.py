from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=70)
    status = models.BooleanField()

    def __str__(self):
        return str(self.nome)


class Administrador (models.Model):
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return str(Pessoa.nome)


class User (models.Model):
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return str(Pessoa.nome)


class Config(models.Model):
    dominio = models.CharField(max_length=200)
    endservidor = models.CharField(max_length=200)
    gadmin = models.CharField(max_length=200)
    ou = models.CharField(max_length=200)
    filter = models.TextField('Filtro')


class Grupo(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    status = models.BooleanField()

    def __str__(self):
        return self.nome

class Camera(models.Model):
    nome = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.nome

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.nome

class Camera_Grupo(models.Model):
    id_camera = models.ForeignKey(Camera, on_delete=models.PROTECT)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    status = models.BooleanField()

class Grupo_Pessoa(models.Model):
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    status = models.BooleanField()

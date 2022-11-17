from django.db import models
from django.conf import settings


class Video (models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    link = models.CharField(max_length=200)
    usuarios = models.ManyToManyField(settings.AUTH_USER_MODEL)
    views = models.IntegerField(default=0)
    publico = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Comentario (models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
    )
    video = models.ForeignKey(Video)
    comentario = models.CharField(max_length=500)

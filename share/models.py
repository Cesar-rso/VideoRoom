from django.db import models
from django.conf import settings


# Create your models here.
class Comentario (models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
    )
    comentario = models.CharField(max_length=500)


class Video (models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    arquivo = models.FileField()
    usuarios = models.ManyToManyField(settings.AUTH_USER_MODEL)
    comentarios = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

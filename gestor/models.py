from django.db import models

# Create your models here.
class Curso(models.Model):
  codigo = models.CharField(primary_key=True, max_length=6)
  nombre = models.CharField(max_length=100)
  creditos = models.PositiveSmallIntegerField()

  def __str__(self):
    texto = "{0}: valor de ({1}) creditos"
    return texto.format(self.nombre, self.creditos,)
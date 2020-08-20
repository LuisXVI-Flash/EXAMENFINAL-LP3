from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Curso(models.Model):
    idcurso = models.IntegerField()
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=120)
    horas = models.CharField(max_length=2)
    creditos=models.IntegerField()
    estado = models.CharField(max_length=1)

    
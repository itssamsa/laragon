from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
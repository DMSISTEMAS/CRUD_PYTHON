from django.db import models

# Create your models here.
class Tareas(models.Model):
    nombre = models.CharField (max_length=100)
    descripcion = models.CharField (max_length=300)

    def __str__ (self):
        return self.nombre
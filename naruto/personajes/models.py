from django.db import models

# Create your models here.
class Personaje(models.Model):
    alias = models.CharField(max_length=30)
    nombre_completo = models.CharField(max_length=30)
    aldea = models.CharField(max_length=30)
    clan = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='personajes/')
    cargado_en = models.DateTimeField(auto_created=True)

    def __str__(self) -> str:
        return f"{self.nombre_completo} {self.clan}"
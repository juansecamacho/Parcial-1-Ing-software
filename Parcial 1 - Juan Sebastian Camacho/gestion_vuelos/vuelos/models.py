from django.db import models

from django.db import models

class Flight(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=(('Nacional', 'Nacional'), ('Internacional', 'Internacional')))
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


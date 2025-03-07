from django.db import models

class Ponto(models.Model):
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"Registro de Ponto em {self.data_hora}"
    
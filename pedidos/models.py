from django.db import models

class Pedido(models.Model):

    descricao = models.CharField(max_length=200)
    valor_total = models.FloatField()
    cliente = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

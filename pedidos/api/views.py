from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from pedidos.api.serializer import PedidosSerializer
from pedidos.models import Pedido


class PedidoViewSet(ModelViewSet):
    serializer_class = PedidosSerializer
    querySet = Pedido.objects.all()


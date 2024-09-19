from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from pedidos.api.serializer import PedidosSerializer, PedidosCreateSerializer
from pedidos.api.serializer import ItemSerializer
from pedidos.models import Pedido
from pedidos.models import Item



class PedidoViewSet(ModelViewSet):
    serializer_class = PedidosSerializer
    queryset = Pedido.objects.all()

    def create(self, request):
        serializer = PedidosCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            pedido = Pedido.objects.create(
                cliente =serializer.validated_data['cliente'],
                endereco =serializer.validated_data['endereco'],
                
            )
            pedido.item.set(serializer.validated_data['item'])
            valor_total = 0.0
            for item in pedido.item.all():
                valor_total += item.preco
            
            pedido.valor_total = valor_total
            pedido.save()

            serializer = PedidosSerializer(pedido)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        

        


class ItemviewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


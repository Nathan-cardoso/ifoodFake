from rest_framework.serializers import ModelSerializer
from pedidos.models import Pedido

class PedidosSerializer(ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['descricao', 'valor_total', 'cliente', 'endereco']
    

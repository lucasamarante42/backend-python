from rest_framework import serializers
from .models import OrderItens

class OrderItensSerializer(serializers.ModelSerializer):  # create class to serializer model
    product_name = serializers.ReadOnlyField(source='product.name')
    total_quantity_order = serializers.ReadOnlyField(source='order.total_quantity')

    class Meta:
        model = OrderItens
        fields = ('id', 'quantity', 'date_order_iten', 'product_name', 'total_quantity_order', 'product', 'order')

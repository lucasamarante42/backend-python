from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):  # create class to serializer model
    client_name = serializers.ReadOnlyField(source='client.name')
    seller_name = serializers.ReadOnlyField(source='seller.name')

    class Meta:
        model = Order
        fields = ('id', 'total_quantity', 'value_total', 'date_order', 'client_name', 'seller_name', 'client', 'seller')

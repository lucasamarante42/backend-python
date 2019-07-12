from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):  # create class to serializer model
    category_description = serializers.ReadOnlyField(source='category.description')

    class Meta:
        model = Product
        fields = ('id', 'description', 'name', 'price', 'category_description', 'category')


class UserAdminSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'products')
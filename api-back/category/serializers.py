from rest_framework import serializers
from .models import Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Category
        fields = ('id', 'description')

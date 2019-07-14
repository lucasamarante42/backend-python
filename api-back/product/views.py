from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Product
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import ProductSerializer
from .pagination import CustomPagination

from datetime import datetime

class get_delete_update_product(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return product

    # Get a product
    def get(self, request, pk):

        product = self.get_queryset(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a product
    def put(self, request, pk):
        
        product = self.get_queryset(pk)

        #if(request.user == product.creator): # If creator is who makes request
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a product
    def delete(self, request, pk):

        product = self.get_queryset(pk)
        product.deleted_at = datetime.now()

        product.save()

        #if(request.user == product.creator): # If creator is who makes request
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_products(ListCreateAPIView):
    serializer_class = ProductSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       products = Product.objects.all().filter(deleted_at__isnull=True)
       return products

    # Get all products
    def get(self, request):
        products = self.get_queryset()
        paginate_queryset = self.paginate_queryset(products)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new product
    def post(self, request):
        
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
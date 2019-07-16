from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import OrderItens

from .serializers import OrderItensSerializer
from .pagination import CustomPagination

from datetime import datetime

class get_delete_update_orders_itens(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItensSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            order_itens = OrderItens.objects.get(pk=pk)
        except OrderItens.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return order_itens

    # Get a order iten
    def get(self, request, pk):

        order_iten = self.get_queryset(pk)
        serializer = OrderItensSerializer(order_iten)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a order iten
    def put(self, request, pk):
        
        order_iten = self.get_queryset(pk)

        #if(request.user == order.creator): # If creator is who makes request
        serializer = OrderItensSerializer(order_iten, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a order iten
    def delete(self, request, pk):

        order_iten = self.get_queryset(pk)

        #if(request.user == order.creator): # If creator is who makes request
        order_iten.deleted_at = datetime.now()

        order_iten.save()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_orders_itens(ListCreateAPIView):
    serializer_class = OrderItensSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       order_itens = OrderItens.objects.all()
       return order_itens

    # Get all order_itens
    def get(self, request):
        order_itens = self.get_queryset()
        paginate_queryset = self.paginate_queryset(order_itens)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new order
    def post(self, request):
        
        serializer = OrderItensSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_orders_itens_by_order_id(ListCreateAPIView):
    serializer_class = OrderItensSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset_by_order(self, order_id):
        try:
            order_itens = OrderItens.objects.all().filter(order=order_id)

        except OrderItens.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return order_itens

    # Get a order iten
    def get(self, request, order_id):
        
        order_itens = self.get_queryset_by_order(order_id)
        
        paginate_queryset = self.paginate_queryset(order_itens)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)
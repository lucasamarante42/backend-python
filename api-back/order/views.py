from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Order

from .serializers import OrderSerializer
from .pagination import CustomPagination

class get_delete_update_orders(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return order

    # Get a order
    def get(self, request, pk):

        order = self.get_queryset(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a order
    def put(self, request, pk):
        
        order = self.get_queryset(pk)

        #if(request.user == order.creator): # If creator is who makes request
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a order
    def delete(self, request, pk):

        order = self.get_queryset(pk)

        #if(request.user == order.creator): # If creator is who makes request
        order.deleted_at = datetime.now()

        order.save()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_orders(ListCreateAPIView):
    serializer_class = OrderSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       orders = Order.objects.all()
       return orders

    # Get all orders
    def get(self, request):
        orders = self.get_queryset()
        paginate_queryset = self.paginate_queryset(orders)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new order
    def post(self, request):
        
        serializer = OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
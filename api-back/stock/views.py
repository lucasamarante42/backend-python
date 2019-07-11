from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Stock

from .serializers import StockSerializer
from .pagination import CustomPagination

from datetime import datetime

class get_delete_update_stock(RetrieveUpdateDestroyAPIView):
    serializer_class = StockSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            stock = Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return stock

    # Get a stock
    def get(self, request, pk):

        stock = self.get_queryset(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a stock
    def put(self, request, pk):
        
        stock = self.get_queryset(pk)

        #if(request.user == stock.creator): # If creator is who makes request
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a stock
    def delete(self, request, pk):

        stock = self.get_queryset(pk)

        #if(request.user == stock.creator): # If creator is who makes request
        stock.deleted_at = datetime.now()

        stock.save()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_stocks(ListCreateAPIView):
    serializer_class = StockSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       stocks = Stock.objects.all()
       return stocks

    # Get all stocks
    def get(self, request):
        stocks = self.get_queryset()
        paginate_queryset = self.paginate_queryset(stocks)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new stock
    def post(self, request):
        
        serializer = StockSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
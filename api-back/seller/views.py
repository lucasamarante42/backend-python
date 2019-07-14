from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Seller
from .serializers import SellerSerializer
from .pagination import CustomPagination

from datetime import datetime

class get_delete_update_seller(RetrieveUpdateDestroyAPIView):
    serializer_class = SellerSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            seller = Seller.objects.get(pk=pk)
        except Seller.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return seller

    # Get a seller
    def get(self, request, pk):

        seller = self.get_queryset(pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a seller
    def put(self, request, pk):
        
        seller = self.get_queryset(pk)

        #if(request.user == seller.creator): # If creator is who makes request
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a seller
    def delete(self, request, pk):

        seller = self.get_queryset(pk)
        seller.deleted_at = datetime.now()

        seller.save()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        
   

class get_post_sellers(ListCreateAPIView):
    serializer_class = SellerSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       sellers = Seller.objects.all().filter(deleted_at__isnull=True)
       return sellers

    # Get all sellers
    def get(self, request):
        sellers = self.get_queryset()
        paginate_queryset = self.paginate_queryset(sellers)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new seller
    def post(self, request):
        
        serializer = SellerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
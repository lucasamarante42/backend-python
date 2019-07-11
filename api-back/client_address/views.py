from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import ClientAddress
from .serializers import ClientAddressSerializer
from .pagination import CustomPagination

from datetime import datetime

class get_delete_update_client_addresses(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientAddressSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            client_address = ClientAddress.objects.get(pk=pk)
        except ClientAddress.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return client_address

    # Get a client address
    def get(self, request, pk):

        client_address = self.get_queryset(pk)
        serializer = ClientAddressSerializer(client_address)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a client
    def put(self, request, pk):
        
        client_address = self.get_queryset(pk)

        #if(request.user == client.creator): # If creator is who makes request
        serializer = ClientAddressSerializer(client_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a client address
    def delete(self, request, pk):

        client_address = self.get_queryset(pk)
        client_address.deleted_at = datetime.now()

        client_address.save()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        
   

class get_post_client_addresses(ListCreateAPIView):
    serializer_class = ClientAddressSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       clients_addresses = ClientAddress.objects.all()
       return clients_addresses

    # Get all clients address
    def get(self, request):
        clients_addresses = self.get_queryset()
        paginate_queryset = self.paginate_queryset(clients_addresses)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new client address
    def post(self, request):
        
        serializer = ClientAddressSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
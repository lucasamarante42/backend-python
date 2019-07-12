from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Client
from .serializers import ClientSerializer
from .pagination import CustomPagination

from datetime import datetime

class get_delete_update_client(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return client

    # Get a client
    def get(self, request, pk):

        client = self.get_queryset(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a client
    def put(self, request, pk):
        
        client = self.get_queryset(pk)

        #if(request.user == client.creator): # If creator is who makes request
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a client
    def delete(self, request, pk):

        client = self.get_queryset(pk)
        client.deleted_at = datetime.now()

        client.save()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        
   

class get_post_clients(ListCreateAPIView):
    serializer_class = ClientSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       clients = Client.objects.all().filter(deleted_at__isnull=True)
       return clients

    # Get all clients
    def get(self, request):
        clients = self.get_queryset()
        paginate_queryset = self.paginate_queryset(clients)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new client
    def post(self, request):
        
        serializer = ClientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
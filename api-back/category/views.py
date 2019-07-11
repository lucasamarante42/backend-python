from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Category
from .serializers import CategorySerializer
from .pagination import CustomPagination

class get_delete_update_category(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return category

    # Get a category
    def get(self, request, pk):

        category = self.get_queryset(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a category
    def put(self, request, pk):
        
        category = self.get_queryset(pk)

        #if(request.user == product.creator): # If creator is who makes request
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a category
    def delete(self, request, pk):

        category = self.get_queryset(pk)

        #if(request.user == product.creator): # If creator is who makes request
        category.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_categories(ListCreateAPIView):
    serializer_class = CategorySerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       categories = Category.objects.all()
       return categories

    # Get all categories
    def get(self, request):
        categories = self.get_queryset()
        paginate_queryset = self.paginate_queryset(categories)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new category
    def post(self, request):
        
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Order
from order_itens.models import OrderItens

from .serializers import OrderSerializer
from .pagination import CustomPagination

from datetime import datetime

import pdfkit
from django.http import HttpResponse
from django.template import Context, Template

from django.conf import settings
from django.template.loader import get_template
from order_itens.serializers import OrderItensSerializer

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
       orders = Order.objects.all().filter(deleted_at__isnull=True)
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

class get_orders_to_pdf(ListCreateAPIView):
    

    def get(self, request, pk):
        serializer_class = OrderItensSerializer
        try:
            order = Order.objects.get(pk=pk)
            order_itens = OrderItens.objects.all().filter(order=pk)
        except Order.DoesNotExist:
            order = None
            order_itens = None
        
        dict_result = {}
        if order:
            serializer = OrderSerializer(order)
            dict_result['order_id'] = serializer.data['id']
            dict_result['client_name'] = serializer.data['client_name']
            dict_result['seller_name'] = serializer.data['seller_name']
            dict_result['total_quantity'] = serializer.data['total_quantity']
            dict_result['value_total'] = serializer.data['value_total']
            dict_result['date_order'] = serializer.data['date_order']

        lst_order_itens =[]
        if order_itens:            
            #print(order_itens.exists())
            serializer_itens = OrderItensSerializer(order_itens, many=True)
            
            for i in serializer_itens.data:                
                lst_order_itens.append({
                    'quantity': i['quantity'],
                    'product_name': i['product_name']
                })

        if dict_result:
            dict_result['lst_order_itens'] = lst_order_itens

        print(dict_result)
        # # Create a URL of our project and go to the template route
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        
        t = get_template(settings.TEMPLATES_HTML + 'order.html')
       
        html = t.render(dict_result)

        pdf = pdfkit.from_string(html, False, options=options)

        # Generate download
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="file_out.pdf"'

        return response

        #return Response(dict_result, 200) #return para testes apenas busca de dados
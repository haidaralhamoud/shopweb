from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductsSerializer 
from .serializer import  OrderSerializer
from products.models import Products
from order.models import Order
from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def apiAll(request):
    api_url={
        'order':'/order/',
        'Create-order':'/create_order/',
        'List':'/products/',
        'Delail View':'/products_delail/<str:pk>',
        'Create' :'/create_products/',
        'Update' : '/update_products/<str:pk>',
        'Delete':'/delete_products/<str:pk>',
    }
    return Response(api_url)


@api_view(['GET'])
def productsList(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def orderList(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order,many=True)
    return Response(serializer.data)

class orderCreate(generics.CreateAPIView):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def productsDelail(request , pk):
    products = Products.objects.get(id = pk)
    serializer = ProductsSerializer(products,many=False)
    return Response(serializer.data)    

# @api_view(['POST', 'GET'])
# def productsCreate(request):
#     serializer = ProductsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)       

class productsCreate(generics.CreateAPIView):
    model = Products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

@api_view(['POST'])
def productsUpdate(request,pk):
    products = Products.objects.get(id = pk)
    serializer = ProductsSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)      

@api_view(['DELETE'])
def productsDelete(request,pk):
    products = Products.objects.get(id = pk)
    products.delete()

    return Response("succsesfully")   
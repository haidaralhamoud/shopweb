from rest_framework import serializers
from products.models import Products
from order.models import Order
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id_products','name','phone','address','locx','locy','quantity')
        
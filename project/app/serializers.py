from rest_framework import serializers
from .models import Product, Bin

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = '__all__'
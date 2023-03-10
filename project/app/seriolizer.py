from rest_framework import serializers
from .models import Product, Producer, Category

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
from rest_framework import serializers
from .models import Pets, Category, StatusPet, Type, StatusOrder, Order

class PerSerialzer(serializers.ModelSerializer):
    class Meta():
        model = Pets
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'

class TypeSeralizer(serializers.ModelSerializer):
    class Meta():
        model = Type
        fields = '__all__'

class StatusPetSerializer(serializers.ModelSerializer):
    class Meta():
        model = StatusPet
        fields = '__all__'

class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = StatusOrder
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = '__all__'
        
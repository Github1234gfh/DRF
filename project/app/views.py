from rest_framework import  viewsets
from .models import Pets, Category, Type, StatusPet, StatusOrder, Order
from .serializers import PerSerialzer, CategorySerializer, TypeSeralizer, StatusPetSerializer, OrderSerializer, StatusOrderSerializer

class ViewPets(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PerSerialzer

class ViewCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ViewStatus(viewsets.ModelViewSet):
    queryset = StatusPet.objects.all()
    serializer_class = StatusPetSerializer

class ViewType(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSeralizer

class ViewOrderStatus(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer

class ViewOrder(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
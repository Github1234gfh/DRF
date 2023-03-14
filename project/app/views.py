from rest_framework import viewsets
from .models import Product, Bin
from .serializer import ProductSerializer, BinSerializer

class ViewProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ViewBin(viewsets.ModelViewSet):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
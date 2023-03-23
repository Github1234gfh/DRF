from django.urls import path, re_path, include
from rest_framework.permissions import IsAuthenticated
from .permitions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Product, Order, Cart
from .serializers import ProductSerializer, CartSerializer, OrderSerializer
from . import views

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('products', views.Allview.as_view(model = Product, serializer_class = ProductSerializer,  permission_classes=[IsAdminOrReadOnly])),
    path('product/<int:pk>', views.Allview.as_view(model = Product, serializer_class = ProductSerializer,  permission_classes=[IsAdminOrReadOnly])),
    path('orders', views.Allview.as_view(model = Order, serializer_class = OrderSerializer, permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ])),
    path('order/<int:pk>', views.Allview.as_view(model = Order, serializer_class = OrderSerializer, permission_classes = [IsAuthenticated, IsOwnerOrReadOnly])),
    path('carts', views.Allview.as_view(model = Cart, serializer_class = CartSerializer, permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ])),
    path('cart/<int:pk>', views.Allview.as_view(model = Cart, serializer_class = CartSerializer, permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ])),
]

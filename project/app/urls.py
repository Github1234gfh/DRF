from django.urls import path
from .serializers import OrderSerializer, CartSerializer
from .models import Order, Cart
from . import views

urlpatterns = [
    path('registration/', views.RegistrationUser.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('logout/', views.LogoutUser.as_view()),
    path('categoryes/', views.CategoryListCrateView.as_view()),
    path('categoryes/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('countryes/', views.CountryListCrateView.as_view()),
    path('countryes/<int:pk>/', views.CountryRetrieveUpdateDestroyAPIView.as_view()),
    path('producers/', views.ProducerListCrateView.as_view()),
    path('producers/<int:pk>/', views.ProducerRetrieveUpdateDestroyAPIView.as_view()),
    path('products/', views.ProductsListCrateView.as_view()),
    path('products/<int:pk>/', views.ProductsRetrieveUpdateDestroyAPIView.as_view()),
    path('orders/', views.CartAndOrderAPIView.as_view(model = Order, serizilizer_class = OrderSerializer, message_on_many = 'Orders')),
    path('orders/<int:pk>/', views.CartAndOrderAPIView.as_view(model = Order, serizilizer_class = OrderSerializer, message_on_one = 'order')),
    path('carts/', views.CartAndOrderAPIView.as_view(model = Cart, serizilizer_class = CartSerializer, message_on_many = 'Carts')),
    path('carts/<int:pk>/', views.CartAndOrderAPIView.as_view(model = Cart, serizilizer_class = CartSerializer, message_on_one = 'cart')),
]
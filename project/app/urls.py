from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.LogoutUser.as_view()),
    path('login', views.LoginUser.as_view()),
    path('registration', views.RegistrationUser.as_view()),
    path('carts', views.ListCreateProduct.as_view()),
    path('cart/<int:pk>', views.RetrieveUpdateDestroyCart.as_view()),
    path('producers', views.ListCreateProducer.as_view()),
    path('producer/<int:pk>', views.RetrieveUpdateDestroyProducer.as_view()),
    path('products', views.ListCreateProduct.as_view()),
    path('product/<int:pk>', views.RetrieveUpdateDestroyProduct.as_view()),
    path('orders', views.ListCreateOrder.as_view()),
    path('order/<int:pk>', views.RetrieveUpdateDestroyOrder.as_view()),
    path('countryes', views.ListCreateCountry.as_view()),
    path('country/<int:pk>', views.RetrieveUpdateDestroyCountry.as_view()),
]

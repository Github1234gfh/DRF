from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ProductView.as_view()),
    path('products/<int:pk>', views.ProductView.as_view()),
    path('categoryes', views.CategoryView.as_view()),
    path('categoryes/<int:pk>', views.CategoryView.as_view()),
    path('produsers', views.ProduserView.as_view()),
    path('produsers/<int:pk>', views.ProduserView.as_view()),
]
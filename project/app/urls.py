from django.urls import path
from . import views
from .models import Order, OrderStatus, Job, Worker
from .serializator import WorkerSerializer, OrderSerializer, OrderStatusSerializer, JobSerializer

urlpatterns = [
    path('workers', views.Allview.as_view(model=Worker, modelserializer=WorkerSerializer)),
    path('workers/<int:pk>', views.Allview.as_view(model=Worker, modelserializer=WorkerSerializer)),
    path('orders', views.Allview.as_view(model=Order, modelserializer=OrderSerializer)),
    path('orders/<int:pk>', views.Allview.as_view(model=Order, modelserializer=OrderSerializer)),
    path('jobs', views.Allview.as_view(model=Job, modelserializer=JobSerializer)),
    path('jobs/<int:pk>', views.Allview.as_view(model=Job, modelserializer=JobSerializer)),
    path('orderstatuses', views.Allview.as_view(model=OrderStatus, modelserializer=OrderStatusSerializer)),
    path('orderstatuses/<int:pk>', views.Allview.as_view(model=OrderStatus, modelserializer=OrderStatusSerializer))
]

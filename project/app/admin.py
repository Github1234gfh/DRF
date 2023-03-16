from django.contrib import admin
from .models import Order, OrderStatus, Worker, Job

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Worker)
admin.site.register(Job)
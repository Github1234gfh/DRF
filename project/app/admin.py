from django.contrib import admin
from .models import Pets, Category, StatusPet, Type, Order, StatusOrder

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(StatusPet)
admin.site.register(Pets)
admin.site.register(Order)
admin.site.register(StatusOrder)

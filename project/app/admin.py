from django.contrib import admin
from .models import Order, Producer, Product, Cart , Category, User, Country

admin.site.register(Order)
admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(User)
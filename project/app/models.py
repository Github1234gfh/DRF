from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)    

    def __str__(self):
        return f'{self.id}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    all_const = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"Order {self.id}, price {self.all_const}"
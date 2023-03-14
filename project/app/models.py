from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30) 
    discription = models.TextField(max_length=300)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
    
class Bin(models.Model):
    name = models.CharField(max_length=30) 
    products = models.ManyToManyField(Product, blank=False)
    total_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
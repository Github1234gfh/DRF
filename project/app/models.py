from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
class Producer(models.Model):
    firm_name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.firm_name

class Product(models.Model):
    title = models.CharField(max_length=30)
    size = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
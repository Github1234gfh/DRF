from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class StatusPet(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pets(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField()
    typr = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusPet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StatusOrder(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Order(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sel_date = models.DateField()
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    complete = models.BooleanField()

    def __str__(self):
        return self.pet.name
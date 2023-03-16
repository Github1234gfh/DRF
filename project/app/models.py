from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField('Name',max_length=30)
    surname = models.CharField('Surname',max_length=30)
    otch = models.CharField('Otchestvo', max_length=30)
    login = models.CharField('Login', max_length=30)
    password = models.CharField('Password', max_length=30)
    photo = models.ImageField('Photo')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OrderStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Order(models.Model):
    table = models.IntegerField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    time_create_order = models.IntegerField('Minutes')
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status)
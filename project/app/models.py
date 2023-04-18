from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Email must be not empty')
        if not username:
            raise ValueError('Username must be not empty')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, username, password, **extra_fields)
            
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email

class Producer(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    producer = models.ForeignKey(Producer, default=1, on_delete=models.CASCADE)
    country_producer = models.ForeignKey(Country, default=1, on_delete=models.CASCADE)
    new = models.BooleanField(default=True)
    cost = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} {self.name}'

class Cart(models.Model):
    
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
    
class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)
    products = models.ManyToManyField(Product)
    all_cost = models.PositiveIntegerField(default=111)

    def __str__(self):
        return f'{self.number}'
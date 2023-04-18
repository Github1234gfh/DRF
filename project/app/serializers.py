from .models import Cart, Producer, Product, Order, Country, User
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    user: User = None
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user:
            return user
        return False

class RegistrationUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = [ 'email', 'username', 'password', 'password2']
    
    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password mismatch'})
        user.set_password(password)
        user.save()
        self.user = user

        return self.user

class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Producer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    all_cost = serializers.IntegerField()

    # def get_total_cost(self, obj):
        
    #     total = 0
    #     for product in Product.objects.all():
    #         if product.id in self.products:
    #              total += product.cost
    #     self.all_cost = total
    #     return total
    
    class Meta:
        model = Order
        fields = '__all__'
    
class CountrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Country
        fields = '__all__'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RegistrationUserSerializer, UserLoginSerializer
from .permisssions import IsAdminOrreadOnly
from django.contrib.auth import logout
from .models import Producer, Product, Order, Country, Cart
from .serializers import ProducerSerializer, ProductSerializer, CartSerializer, CountrySerializer, OrderSerializer

class ListCreateProducer(ListCreateAPIView):
    queryset  = Producer.objects.all()
    serializer_class  = ProducerSerializer
    permission_classes = [IsAdminOrreadOnly, ]

class RetrieveUpdateDestroyProducer(RetrieveUpdateDestroyAPIView):
    queryset  = Producer.objects.all()
    serializer_class  = ProducerSerializer
    permission_classes = [IsAdminOrreadOnly, ]

class ListCreateProduct(ListCreateAPIView):
    queryset  = Product.objects.all()
    serializer_class  = ProductSerializer

class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):
    queryset  = Product.objects.all()
    serializer_class  = ProductSerializer

class ListCreateOrder(ListCreateAPIView):
    queryset  = Order.objects.all()
    serializer_class  = OrderSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response({'messege': 'Order is empty'})

class RetrieveUpdateDestroyOrder(RetrieveUpdateDestroyAPIView):
    queryset  = Order.objects.all()
    serializer_class  = OrderSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.get(pk=pk)
        if order.user == request.user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        return Response({'messege': 'Order is empty'})

class ListCreateCountry(ListCreateAPIView):
    queryset  = Country.objects.all()
    serializer_class  = CountrySerializer
    permission_classes = [IsAdminUser,]

class RetrieveUpdateDestroyCountry(RetrieveUpdateDestroyAPIView):
    queryset  = Country.objects.all()
    serializer_class  = CountrySerializer
    permission_classes = [IsAdminUser,]

class ListCreateCart(ListCreateAPIView):
    queryset  = Cart.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        carts = Cart.objects.filter(user=user)
        serializer = CartSerializer(carts, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response({'messege': 'Cart is empty'})

class RetrieveUpdateDestroyCart(RetrieveUpdateDestroyAPIView):
    queryset  = Cart.objects.all()
    serializer_class  = CartSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cart = Cart.objects.get(pk=pk)
        if (cart.user == request.user):
            serializer = CartSerializer(cart, many=False)
            return Response(serializer.data)
        return Response({'messege': 'Cart is empty'})

class RegistrationUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['data'] = serializer.data
            user = serializer.user
            token = Token.objects.create(user=user)
            return Response({'user_token': token.key}, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    def post(self, request, *args, **kwargs):
        serizlier = UserLoginSerializer(data=request.data)

        if not serizlier.is_valid():
            return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED) 
        user = serizlier.validated_data
        if user:
            token_object, token_created = Token.objects.get_or_create(user=user)
            token = token_object if token_object else token_created

            return Response({'user_token': token.key}, status=status.HTTP_200_OK) 
        return Response({'error': {'messege': 'Authentication failed'}}, status=status.HTTP_400_BAD_REQUEST)

class LogoutUser(APIView):
    def get(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except(AttributeError):
            return Response({"error": {'messege': 'logout failed'}}, status=status.HTTP_400_BAD_REQUEST)
        logout(request)
        return Response({'messege': 'logout'}, status=status.HTTP_200_OK)

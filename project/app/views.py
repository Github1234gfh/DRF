from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import OnlyGetOrAadmin
from .serializers import RegistrationUserSerializer, UserLoginSerializer, ProductSerializer, CategorySerializer, CountrySerializer, ProducerSerializer 
from .models import Order, Product, Country, Producer, Category

class CategoryListCrateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class ProducerListCrateView(ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [IsAdminUser]

class ProducerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [IsAdminUser]

class CountryListCrateView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class ProductsListCrateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [OnlyGetOrAadmin]

class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [OnlyGetOrAadmin]

class CartAndOrderAPIView(APIView):

    permission_classes = [IsAuthenticated,]

    model = None
    serizilizer_class = None
    message_on_many = None
    message_on_one = None

    def get(self, request, *args, **kvargs):
        pk = kvargs.get('pk', None)
        if not pk:
            objects = self.model.objects.filter(user=request.user)
            seriazlier = self.serizilizer_class(objects, many=True)
            if seriazlier.data:
                return Response(seriazlier.data)
            return Response({'message': f'{self.message_on_many} is empty'})
        try:
            object = self.model.objects.get(pk=pk)
            if (object.user == request.user):
                serializer = self.serizilizer_class(object, many=False)
                return Response(serializer.data)
            return Response({"message": f"You dont't have this {self.message_on_one}"})
        except:
            return Response({"message": f"Not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serizalizer = self.serizilizer_class(data = request.data, context={'request': request})
        if serizalizer.is_valid():
            serizalizer.save()
            return Response(serizalizer.data, status=status.HTTP_201_CREATED)
        return Response(serizalizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kvargs):
        if self.model == Order:
            return Response({"message": "Can't put order"})
        pk = kvargs.get('pk', None)

        try:
            object = self.model.objects.get(pk=pk)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if object.user == request.user:
            serializer = self.serizilizer_class(data = request.data, context={'request': request}, instance=object)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': ' Is not your item'})
    
    def delete(self, request, *args, **kvargs):
        if self.model == Order:
            return Response({"message": "Can't delete order"})
        pk = kvargs.get('pk', None)

        try: 
            object = self.model.objects.get(pk=pk)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if object.user == request.user:
            object.delete()
            return Response({'message': f'deleted {str(pk)}'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Is not your item'})

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

    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):

        try:
            request.user.auth_token.delete()
        except(AttributeError):
            return Response({"error": {'messege': 'logout failed'}}, status=status.HTTP_400_BAD_REQUEST)
        logout(request)
        return Response({'messege': 'logout'}, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import JanrSerializer, ActerSerializer, MovieSerializer, CategorySerializer, CommentSerializer, RegistrationUserSerializer, UserLoginSerializer
from .models import Janr, Acter, Movie, Category, Comment

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
        return Response({"message": "Logout"}, status=status.HTTP_200_OK)

class JanrListCreate(ListCreateAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer
    permission_classes = [IsAdminUser,]

class JanrRetrie(RetrieveUpdateDestroyAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer
    permission_classes = [IsAdminUser,]

class ActerListCreate(ListCreateAPIView):
    queryset = Acter.objects.all()
    serializer_class = ActerSerializer
    permission_classes = [IsAdminUser,]

class ActerRetrie(RetrieveUpdateDestroyAPIView):
    queryset = Acter.objects.all()
    serializer_class = ActerSerializer
    permission_classes = [IsAdminUser, ]

class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrie(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser,]

class CategoryRetrie(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser,]

class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

class CommentRetrie(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]


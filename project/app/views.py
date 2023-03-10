from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category, Producer
from .seriolizer import ProductSerializer, CategorySerializer, ProducerSerializer
from django.forms import model_to_dict

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})
    
    def post(self, request):
        seriolizer = ProductSerializer(data=request.data)
        seriolizer.is_valid(raise_exception=True)
        seriolizer.save()
        return Response({'category': seriolizer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error':"object doesnt exist"})

        try:
            isinstance = Product.objects.get(pk=pk)
        except:
            return Response({'error': 'object is not exist'})
        
        seriolizer = ProductSerializer(data=request.data, instance=isinstance)
        seriolizer.is_valid(raise_exception=True)
        seriolizer.save()
        return Response({'post': seriolizer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error':"object doesnt exist"})
        
        producer = Product.objects.get(pk=pk)
        producer.delete()
        return Response({"producer": f"delete {str(pk)}"})

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({'categoryes': serializer.data})

    def post(self, request):
        seriolizer = CategorySerializer(data=request.data)
        seriolizer.is_valid(raise_exception=True)
        seriolizer.save()
        return Response({'category': seriolizer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error':"object doesnt exist"})

        try:
            isinstance = Category.objects.get(pk=pk)
        except:
            return Response({'error': 'object is not exist'})
        
        seriolizer = CategorySerializer(data=request.data, instance=isinstance)
        seriolizer.is_valid(raise_exception=True)
        seriolizer.save()
        return Response({'post': seriolizer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error':"object doesnt exist"})
        
        producer = Category.objects.get(pk=pk)
        producer.delete()
        return Response({"producer": f"delete {str(pk)}"})

class ProduserView(APIView):
    def get(self, request):
        producer = Producer.objects.all()
        serializer = ProducerSerializer(producer, many=True)
        return Response({'producers': serializer.data})

    def post(self, request):
        seriolizer = ProducerSerializer(data=request.data)
        seriolizer.is_valid(raise_exception=True)
        seriolizer.save()
        return Response({'category': seriolizer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error':"object doesnt exist"})
        
        producer = Producer.objects.get(pk=pk)
        producer.delete()
        return Response({"producer": f"delete {str(pk)}"})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error':"object doesnt exist"})

        try:
            isinstance = Producer.objects.get(pk=pk)
        except:
            return Response({'error': 'object is not exist'})
        
        seriolizer = ProducerSerializer(data=request.data, instance=isinstance)
        seriolizer.is_valid(raise_exception=True)
        seriolizer.save()
        return Response({'post': seriolizer.data})
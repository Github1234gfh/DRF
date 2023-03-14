from rest_framework import serializers
from .models import Films, Article, Janr, Directior


class DirectiorSeriolizer(serializers.ModelSerializer):
    class Meta:
        model = Directior
        fields = '__all__'

class JanrSeriolizer(serializers.ModelSerializer):
    class Meta:
        model = Janr
        fields = '__all__'
        

class FilmsSeriolizer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'

class ArticleSeriolizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
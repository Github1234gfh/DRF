
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from .seriolizer import FilmsSeriolizer, JanrSeriolizer, DirectiorSeriolizer, ArticleSeriolizer
from .models import Films, Article, Directior, Janr

class ViewFilms(ListCreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSeriolizer

class ViewFilm(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSeriolizer

class ViewDirectors(ListCreateAPIView):
    queryset = Directior.objects.all()
    serializer_class = DirectiorSeriolizer

class ViewDirector(RetrieveUpdateDestroyAPIView):
    queryset = Directior.objects.all()
    serializer_class = DirectiorSeriolizer

class ViewJanrs(ListCreateAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSeriolizer

class ViewJanr(RetrieveUpdateDestroyAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSeriolizer

class ViewArticles(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSeriolizer

class ViewArticle(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSeriolizer

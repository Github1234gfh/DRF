from django.urls import path
from .views import ViewFilm , ViewFilms, ViewDirector,  ViewDirectors , ViewJanr, ViewJanrs, ViewArticle, ViewArticles


urlpatterns = [
    path('films', ViewFilms.as_view()),
    path('films/<int:pk>', ViewFilm.as_view()),
    path('directors', ViewDirectors.as_view()),
    path('directors/<int:pk>', ViewDirector.as_view()),
    path('janrs', ViewJanrs.as_view()),
    path('janrs/<int:pk>', ViewJanr.as_view()),
    path('articles', ViewArticles.as_view()),
    path('articles/<int:pk>', ViewArticle.as_view())
]
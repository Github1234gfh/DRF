from django.urls import path, include
from . import views


urlpatterns = [
    path('registration/', views.RegistrationUser.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('logout/', views.LogoutUser.as_view()),
    path('api/janrs/', views.JanrListCreate.as_view()),
    path('api/janrs/<int:pk>/', views.JanrRetrie.as_view()),
    path('api/movies/', views.MovieListCreate.as_view()),
    path('api/movies/<int:pk>/', views.MovieRetrie.as_view()),
    path('api/review/', views.CommentListCreate.as_view()),
    path('api/review/<int:pk>/', views.CommentRetrie.as_view()),
    path('api/cat/', views.CategoryListCreate.as_view()),
    path('api/cat/<int:pk>', views.CategoryRetrie.as_view()),
    path('api/actors/', views.ActerListCreate.as_view()),
    path('api/actors/<int:pk>/', views.ActerRetrie.as_view()),
]

from django.urls import path
from .views import *


urlpatterns = [ 
    path('book/<int:pk>/', get_book_by_id), 
    path('books/', get_books), 
    path('create_book/', create_book), 
    path('update_book/<int:pk>/', update_book), 
    path('delete_book/<int:pk>/', delete_book), 
]
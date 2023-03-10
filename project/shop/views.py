from django.http import JsonResponse 
from rest_framework.decorators import api_view 
 
from .models import Book
from .seriolizer import BookSerializer 
 
 
@api_view(['GET']) 
def get_book_by_id(response, *args, **kwargs): 
    book = Book.objects.get(pk=kwargs['pk']) 
 
    return JsonResponse({'Book': BookSerializer(book, many=False).data}) 
 
 
@api_view(['GET']) 
def get_books(request, *args, **kwargs): 
    books = Book.objects.all() 
 
    return JsonResponse({'Books': BookSerializer(books, many=True).data}) 
 
 
@api_view(['POST']) 
def create_book(request, *args, **kwargs): 
    serializer = BookSerializer(data=request.data) 
    serializer.is_valid(raise_exception=True) 
    serializer.save() 
 
    return JsonResponse({'Book': serializer.data}, status=201) 
 
 
@api_view(['PATCH']) 
def update_book(request, *args, **kwargs): 
    try: 
        book = Book.objects.get(pk=kwargs['pk']) 
    except Book.DoesNotExist: 
        return JsonResponse({'error': 'Book not found'}) 
 
    serializer = BookSerializer(instance=book, data=request.data, partial=True) 
    serializer.is_valid() 
    serializer.save() 
 
    return JsonResponse({'Book': serializer.data}) 
 
 
@api_view(['DELETE']) 
def delete_book(request, *args, **kwargs): 
    try: 
        book = Book.objects.get(pk=kwargs['pk']) 
    except Book.DoesNotExist: 
        return JsonResponse({'error': 'Book not found'}) 
 
    book.delete() 
 
    return JsonResponse({'message': "book was deleted"})
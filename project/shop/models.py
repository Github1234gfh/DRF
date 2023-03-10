from django.db import models

class Book(models.Model):
    title_book = models.CharField(max_length=20, help_text='Title book')
    author = models.CharField(max_length=20, help_text='Author')
    annotations = models.CharField(max_length=20, help_text='Annotations')


    def __str__(self):
        return self.title_book
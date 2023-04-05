from django.contrib import admin
from .models import User, Category, Janr, Comment, Movie, Acter

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Janr)
admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(Acter)

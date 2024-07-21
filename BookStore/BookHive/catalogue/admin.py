from django.contrib import admin
from .models import Genre, SubGenre, Book

admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Book)

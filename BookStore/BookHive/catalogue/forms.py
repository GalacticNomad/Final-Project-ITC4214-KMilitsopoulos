from django import forms
from .models import Book, Genre, SubGenre, Rating


#setting up forms for books genres subgenre and rating
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image', 'genre', 'sub_genre']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class SubGenreForm(forms.ModelForm):
    class Meta:
        model = SubGenre
        fields = ['name', 'genre']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
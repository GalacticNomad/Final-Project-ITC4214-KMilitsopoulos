from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#The classes are defining  the genres books subgnres and rating 


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubGenre(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title

     # Method to get the absolute URL for the book's detail view
    def get_absolute_url(self):
        return reverse('catalogue:book_detail', kwargs={'pk': self.pk})
        # kwargs={'pk': self.pk} passes the primary key of the book as a keyword argument


# ForeignKey to link the rating to a book
# on_delete=models.CASCADE ensures that if the book is deleted, all associated ratings are also deleted
# related_name='ratings' allows reverse lookup from the book to its ratings
class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    # IntegerField to store the rating value

    def __str__(self):
        return f'{self.book.title} - {self.rating} stars'
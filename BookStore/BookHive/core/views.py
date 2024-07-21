from django.shortcuts import render
from catalogue.models import Book

# Create your views here.
# Define the view functions to handle requests for the pages
# Return the HTTP responses rendered from the core html templates

def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

# Retrieve the 10 most recent Book objects from the database
def home(request):
    books = Book.objects.all()[:10] 
    return render(request, 'core/home.html', {'books': books})


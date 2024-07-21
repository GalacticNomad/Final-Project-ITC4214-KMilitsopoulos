from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, SubGenre, Book
from django.db.models import Q, Avg
from django.http import JsonResponse
from .models import Book, Rating
from .forms import BookForm, GenreForm, SubGenreForm, RatingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'catalogue/genres.html', {'genres': genres})

def subgenre_list(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    subgenres = SubGenre.objects.filter(genre=genre)
    return render(request, 'catalogue/subgenres.html', {'subgenres': subgenres, 'genre': genre})

def book_list(request, subgenre_id=None):
    if subgenre_id:
        subgenre = get_object_or_404(SubGenre, id=subgenre_id)
        books = Book.objects.filter(sub_genre=subgenre)
        return render(request, 'catalogue/books.html', {'books': books, 'subgenre': subgenre})
    else:
        books = Book.objects.all()
        return render(request, 'catalogue/book_list.html', {'books': books})


@login_required
def add_book(request):
    if not request.user.profile.is_moderator:
        return redirect('home')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('catalogue:moderator_panel')
    else:
        form = BookForm()
    
    return render(request, 'catalogue/add_book.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    rating_form = RatingForm()

    average_rating = book.ratings.aggregate(average=Avg('rating'))['average']
    
    return render(request, 'catalogue/book_detail.html', {
        'book': book,
        'rating_form': rating_form,
        'average_rating': average_rating,
    })

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'catalogue/book_search_results.html', {'books': books, 'query': query})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('catalogue:moderator_panel')

@login_required
def moderator_panel(request):
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')

    books = Book.objects.all()
    genres = Genre.objects.all()
    subgenres = SubGenre.objects.all()
    return render(request, 'catalogue/moderator_panel.html', {'books': books, 'genres': genres, 'subgenres': subgenres})



@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('catalogue:moderator_panel')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'catalogue/edit_book.html', {'form': form})


@login_required
def manage_genres(request):
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    genres = Genre.objects.all()
    subgenres = SubGenre.objects.all()
    return render(request, 'catalogue/manage_genres.html', {'genres': genres, 'subgenres': subgenres})

@login_required
def add_genre(request):
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genre added successfully!')
            return redirect('catalogue:manage_genres')
    else:
        form = GenreForm()
    
    return render(request, 'catalogue/add_genre.html', {'form': form})

@login_required
def add_subgenre(request):
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        form = SubGenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SubGenre added successfully!')
            return redirect('catalogue:manage_genres')
    else:
        form = SubGenreForm()
    
    return render(request, 'catalogue/add_subgenre.html', {'form': form})

@login_required
def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    genre.delete()
    messages.success(request, 'Genre deleted successfully!')
    return redirect('catalogue:manage_genres')


@login_required
def delete_subgenre(request, subgenre_id):
    subgenre = get_object_or_404(SubGenre, id=subgenre_id)
    if not request.user.profile.is_moderator and not request.user.is_superuser:
        return redirect('home')
    
    subgenre.delete()
    messages.success(request, 'SubGenre deleted successfully!')
    return redirect('catalogue:manage_genres')


@login_required
@require_POST
def submit_rating(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = RatingForm(request.POST)
    if form.is_valid():
        rating, created = Rating.objects.update_or_create(
            book=book, user=request.user,
            defaults={'rating': form.cleaned_data['rating']}
        )
        return JsonResponse({'success': True, 'rating': rating.rating})
    return JsonResponse({'success': False}, status=400)
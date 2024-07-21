from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', views.subgenre_list, name='subgenre_list'),
    path('subgenres/<int:subgenre_id>/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/', views.book_list, name='book_list'),
    path('moderator_panel/', views.moderator_panel, name='moderator_panel'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('manage_genres/', views.manage_genres, name='manage_genres'),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('add_subgenre/', views.add_subgenre, name='add_subgenre'),
    path('delete_genre/<int:genre_id>/', views.delete_genre, name='delete_genre'),
    path('delete_subgenre/<int:subgenre_id>/', views.delete_subgenre, name='delete_subgenre'),
    path('submit_rating/<int:book_id>/', views.submit_rating, name='submit_rating'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
]


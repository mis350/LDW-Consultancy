from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('reviews/',views.ReviewListView.as_view(), name="review-list"),
    path('add/review/', views.create_review, name="add-review"),
    path('book/<int:primary_key>', views.book_detail, name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(), name='author-detail'),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
]




from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('review/<int:s>/',views.show_review, name="show-review"),
    path('create/review/', views.create_review, name="create-review"),
    path('book/<int:primary_key>', views.book_detail, name='book-detail'),
]



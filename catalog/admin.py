from django.contrib import admin
from .models import Author, Genre, Book, BookStatus, Reader, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookStatus)
admin.site.register(Reader)
admin.site.register(Review)
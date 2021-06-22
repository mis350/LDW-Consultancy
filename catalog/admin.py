from django.contrib import admin
from .models import Book, Author, BookStatus, Reader, Genre, Review
# Register your models here.

class BooksInline(admin.TabularInline):
  model = Book
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)
inlines = [BooksInline]

class BookStatusInline(admin.TabularInline):
  model = BookStatus

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BookStatusInline]


@admin.register(BookStatus)
class BookStatusAdmin(admin.ModelAdmin):
  list_display = ('book', 'status', 'borrower', 'due_back', 'id')
  list_filter = ('status', 'due_back')

  fieldsets = (
    (None, {'fields': ('book', 'imprint', 'id')}),
    ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
  )












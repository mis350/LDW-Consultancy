from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
from datetime import date


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter a book genre (e.g. Non-Fiction, Fiction etc.)")

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text=
        '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    genre = models.ManyToManyField(Genre,
                                   help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookStatus(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1,
                              choices=LOAN_STATUS,
                              blank=False,
                              default='a')

    
    def is_overdue(self):
      if self.due_back and date.today() > self.due_back:
        return True
      return False


    class Meta:
       permissions = (("can_mark_returned", "Set book as returned"),)
       ordering = ['due_back']
       verbose_name_plural = "Book Statuses"

    def __str__(self):
        return f' ({self.book.title}) {self.status}'


class Reader(models.Model):
    first_name = models.CharField(max_length=50, null=True, default='')
    last_name = models.CharField(max_length=50, )
    student_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Author(models.Model):
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="DOB")
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Review(models.Model):
    review_text = models.TextField()
    reader_name = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   default='anonymous')
    created_on = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.book}, {self.created_on}'
    def get_absolute_url(self):
      return reverse('book-detail', args=[str(self.id)])


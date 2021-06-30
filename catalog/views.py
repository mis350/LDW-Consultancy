from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, BookForm
from .models import Book, Author, BookStatus, Genre, Review
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here
class MyView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
  


class MyView2(PermissionRequiredMixin):
    permission_required = 'catalog.can_mark_returned'
    # Or multiple permissions
    permission_required = ('catalog.can_mark_returned')

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    on_loan = BookStatus.objects.filter(status__exact='o').count()

    # Available books (status = 'a')
    num_books_available = BookStatus.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    #fic_genre = Genre.objects.filter(name__iexact='Fiction')

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    data = {
        'num_books': num_books,
        'on_loan':  on_loan,
        'num_books_available': num_books_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=data)


class ReviewListView(generic.ListView):
  model = Review
  context_object_name = 'review_list' 
  queryset = Review.objects.all() 
  template_name ='review_list.html'  
  

def create_review(request):
  data = {}
  f = ReviewForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("review-list")
  return render(request, "add_review.html", context=data)

class BookListView(generic.ListView):
  model = Book
  context_object_name = 'book_list' 
  queryset = Book.objects.all() 
  template_name ='book_list.html'  

def book_detail(request, primary_key):
  book = get_object_or_404(Book, pk=primary_key)
  return render(request, 'book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    queryset = Author.objects.all() 
    template_name ='author_list.html'  
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'


class GenreListView(generic.ListView):
  model = Genre
  context_object_name = 'genre_list'
  queryset = Genre.objects.all() 
  template_name ='genre_list.html'  
  paginate_by = 20

def reserve_book(request):
  data = {}
  f = BookForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("book-reserved")
  return render(request, "reserve.html", context=data)

def reserve_complete(request):
  data={}
  return render(request,"complete.html", context=data)


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookStatus
    template_name ='bookstatus_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookStatus.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
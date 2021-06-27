from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Book, Author, BookStatus, Genre, Reader, Review
from django.views import generic

# Create your views here.
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
        #'fic_genre': fic_genre
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=data)


def show_review(request, s):
  obj = get_object_or_404(Review, pk=s)
  reviews = obj.review_set.all()

  data = {}
  data["book"] = obj
  data["review_list"] = reviews
  
  f = ReviewForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("book_list", s=obj.pk)

  return render(request, "book_detail.html", context=data)

def create_review(request):
  f = ReviewForm(request.POST or None)

  data = {}
  data["form"] = f

  if f.is_valid():
    review = f.save(commit=False)
    review.save()
    return redirect("show-review", t=review.title)
  return render(request, "create_review.html", context=data)

class BookListView(generic.ListView):
  model = Book
  context_object_name = 'book_list' 
  queryset = Book.objects.all() 
  template_name ='book_list.html'  

#def book_detail(request, primary_key):
  #book = get_object_or_404(Book, pk=primary_key)
  #return render(request, 'catalog/book_detail.html', context={'book': book})

  
from django import forms
from .models import Review, BookStatus

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ["book", "review_text", "reader_name"]

class BookForm(forms.ModelForm):
  class Meta:
    model = BookStatus
    fields = ["book",]
    

from django import forms
from .models import Book
class BookForm(forms.Form):
    name=forms.CharField(label='Your Name')
    phone=forms.CharField(label='Phone Number')
    date=forms.CharField(label='Date for Photo Taking')
    
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        widgets = {
            'date': forms.DateInput(attrs={  
                'type':'date',
                'class': 'form-control',
                'data-target': '#datetimepicker1'
                }),
        }
    
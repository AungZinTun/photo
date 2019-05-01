from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Session
from .forms import BookForm

# Create your views here.
def index(request):
    session=Session.objects.all()
    return render (request, 'price/index.html', {'session':session})

def book(request):
    if  request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Booking successful, Thank you')
            try:
                form.save()
                return redirect('/')
            except:
                pass
        
    else:
        form=BookForm()
    return render (request, 'price/book.html', {'form':form})

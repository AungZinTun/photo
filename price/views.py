from django.shortcuts import render
from .models import Session

# Create your views here.
def index(request):
    session=Session.objects.all()
    return render (request, 'price/index.html', {'session':session})
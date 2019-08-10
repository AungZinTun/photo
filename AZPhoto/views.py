from django.shortcuts import render
from portfolio.models import Photo
# Create your views here.
def home(request):
    photo= Photo.objects.all()
    return render (request, 'home.html', {'photo':photo })
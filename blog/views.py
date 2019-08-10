from django.shortcuts import render
from portfolio.models import Photo
# Create your views here.
def index(request):
    photo= Photo.objects.all()
    return render (request, 'blog/index.html', {'photo':photo })
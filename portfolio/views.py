from .choices import cat_choices
from django.shortcuts import render
from .models import Photo , Album
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import cat_choices

# Create your views here.
def index(request):
    cat=cat_choices
    photos= Photo.objects.all()

    paginator= Paginator(photos,10 )
    page=request.GET.get('page')
    photo=paginator.get_page(page)
    return render (request, 'portfolio/index.html', {'photo': photo, 'cat':cat })


def cat(request):
    photos= Photo.objects.all()

    if 'cat' in request.GET:
        cat=request.GET['cat']
        if cat:
            photo_cat=photos.filter(category=cat  )


    paginator= Paginator(photo_cat,10 )
    page=request.GET.get('page')
    photo=paginator.get_page(page)
    return render (request, 'portfolio/cat.html', {'photo': photo})

from django.shortcuts import render
from .models import Manga


def home(request):
    context = {
        'data': Manga.objects.all(),
    }
    return render(request, 'reviews/home.html', context)


def about(request):
    return render(request, 'reviews/about.html', {'title': 'About Us'})

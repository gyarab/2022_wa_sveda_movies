# Create your views here.

from django.shortcuts import render

from .models import Movie


def homepage(request):
    context = {
        "movies": Movie.objects.all(),
    }
    return render(request, 'main.html', context)


def directors(request):
    context = {
        "directors": Movie.objects.all(),
    }
    return render(request, 'directors.html', context)

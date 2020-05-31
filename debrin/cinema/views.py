from django.shortcuts import render
from .models import Film


def library(request):
    data = dict()
    films = Film.objects.all()
    data['films'] = films
    return render(request, 'cinema/library.html', context=data)


def film(request, fid):
    data = dict()
    film_id = Film.objects.get(id=fid)
    data['film'] = film_id
    return render(request, 'cinema/film.html', context=data)

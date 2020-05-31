from django.shortcuts import render
from .models import Theatre


def index(request):
    data = dict()
    performances = Theatre.objects.all()
    data['performances'] = performances
    return render(request, 'theatre/index.html', context=data)


def performance(request, tid):
    data = dict()
    theatre_id = Theatre.objects.get(id=tid)
    data['performance'] = theatre_id
    return render(request, 'theatre/performance.html', context=data)

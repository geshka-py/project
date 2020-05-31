from django.shortcuts import render
from .models import TVProgram


def index(request):
    data = dict()
    programs = TVProgram.objects.all()
    data['programs'] = programs
    return render(request, 'programs/index.html', context=data)


def program(request, pid):
    data = dict()
    program_id = TVProgram.objects.get(id=pid)
    data['program'] = program_id
    return render(request, 'programs/program.html', context=data)

from django.shortcuts import render
from .models import Interview


def index(request):
    data = dict()
    interviews = Interview.objects.all()
    data['interviews'] = interviews
    return render(request, 'interview/index.html', context=data)


def interview(request, iid):
    data = dict()
    interview_id = Interview.objects.get(id=iid)
    data['interview'] = interview_id
    return render(request, 'interview/interview.html', context=data)

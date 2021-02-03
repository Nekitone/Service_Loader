from django.shortcuts import render

from .models import Dimresgenforecastmodel


def index(request):
    latest_question_list = Dimresgenforecastmodel.objects.all()
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'importer/index.html', context)

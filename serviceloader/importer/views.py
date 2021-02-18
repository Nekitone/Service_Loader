from django.shortcuts import render
from . import forms


def retrain_service(request):
    form = forms.ServiceForm(request.POST)
    if form.is_valid():
        return render(request, 'importer/retrain_selections.html')
    else:
        form = forms.ServiceForm()
    return render(request, 'importer/retrain_service.html', {'form': form})


def retrain_selections(request):
    name = request.POST['Service_Name']
    context = {
        'selected_choices': [name],
    }
    return render(request, 'importer/retrain_selections.html', context)


def create_service(request):
    form = forms.NewServiceForm(request.POST)
    if form.is_valid():
        return render(request, 'importer/selections.html')
    else:
        form = forms.NewServiceForm()
    return render(request, 'importer/create_service.html', {'form': form})


def selections(request):
    area = request.POST['Area']
    typecode = request.POST['TypeCode']
    name = request.POST['Model_Name']
    context = {
        'selected_choices': [area, typecode, name],
    }
    return render(request, 'importer/selections.html', context)

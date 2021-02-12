from django.shortcuts import render
from .forms import NewServiceForm


def index(request):
    form = NewServiceForm(request.POST)
    if form.is_valid():
        return render(request, 'importer/selections.html')
    else:
        form = NewServiceForm()
    return render(request, 'importer/index.html', {'form': form})


def selections(request):
    country = request.POST['country']
    areatypecode = request.POST['areatypecode']
    name = request.POST['name']
    context = {
        'selected_choices': [country, areatypecode, name],
    }
    return render(request, 'importer/selections.html', context)

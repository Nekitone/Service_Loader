from django.urls import path
from . import views

app_name = 'importer'
urlpatterns = [
    path('', views.index, name='index'),
    path('selections', views.selections, name='selections'),
]

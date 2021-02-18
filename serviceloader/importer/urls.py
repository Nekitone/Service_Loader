from django.urls import path
from . import views

app_name = 'importer'
urlpatterns = [
    path('', views.retrain_service, name='retrain_service'),
    path('retrain_selections', views.retrain_selections, name='retrain_selections'),
    path('create_service', views.create_service, name='create_service'),
    path('selections', views.selections, name='selections'),
]

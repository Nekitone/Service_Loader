from django import forms
from . import models


class ServiceForm(forms.Form):
    Service_Name = forms.ModelChoiceField(queryset=models.Dimresgenforecastservice.objects.values_list('Service_Name', flat=True),
                                  initial=0)


class NewServiceForm(forms.Form):
    Area = forms.CharField(label='Area')
    TypeCode = forms.CharField(label='TypeCode')
    Model_Name = forms.ModelChoiceField(queryset=models.Dimresgenforecastmodel.objects.values_list('Model_Name', flat=True),
                                  initial=0)

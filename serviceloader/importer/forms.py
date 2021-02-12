from django import forms
from . import models


class NewServiceForm(forms.Form):
    country = forms.CharField(label='Country')
    areatypecode = forms.CharField(label='AreaTypeCode')
    name = forms.ModelChoiceField(queryset=models.Dimresgenforecastmodel.objects.values_list('name', flat=True),
                                  initial=0)

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render

from example.sample import forms


def index(request):
    data = {'form': forms.SelectForm(), 'modelform': forms.ModelSelectForm()}

    return render(request, "multiselect/index.html", data)


def index2(request):
    data = {'form': forms.SelectForm2(), 'modelform': forms.ModelSelectForm2()}

    return render(request, "multiselect/index.html", data)

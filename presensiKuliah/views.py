from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

# from .models import presensi

# Create your views here.

def index(request):
    context = {
        'appGroup':'Presensi',
        'appName':'Presensi Kuliah',
    }
    return render (request,'presensiKuliah/index.html',context)
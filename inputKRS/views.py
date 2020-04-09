from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'appGroup':'Mahasiswa',
        'appName' : 'Input KRS',
    }
    return render(request,'inputKRS/index.html',context)
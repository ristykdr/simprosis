from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'appGroup':'Laporan',
        'appName':'Rekap KRS',
    }
    return render(request,'rekapKRS/index.html',context)
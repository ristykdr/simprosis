from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'appGroup':'Laporan',
        'appName':'Rekap RPS',
    }
    return render(request,'rekapRPS/index.html',context)
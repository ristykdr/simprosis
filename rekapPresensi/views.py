from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'appGroup':'Laporan',
        'appName':'Rekap Presensi',
    }
    return render(request,'rekapPresensi/index.html',context)
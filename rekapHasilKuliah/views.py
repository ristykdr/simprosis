from django.shortcuts import render

# Create your views here.
def index (request):
    context={
        'appGroup':'Laporan',
        'appName':'Rekap Hasil Kuliah',
    }
    return render(request,'rekapHasilKuliah/index.html',context)
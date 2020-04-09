from django.shortcuts import render,redirect
from . forms import dosenForm
from .models import dosen
from django.contrib import messages

# Create your views here.
def index (request) :
    semua_dosen = dosen.objects.all()
    context = {
        'appGroup' : 'Operasional',
        'appName' : 'Olah Data Dosen',
        'semua_dosen':semua_dosen
    }
    return render(request,'olahDataDosen/index.html',context)

def create(request):
    pesan=None
    formDosen = dosenForm(request.POST or None)
    if request.method=='POST':
        if formDosen.is_valid():
            formDosen.save()
            pesan='berhasil'
            return redirect('olahDataDosen:index')
        else:
            pesan='Gagal menyimpan. User atau NIDN sudah, ada silahkan pilih User atau NIDN lain  '

    context={
        'appGroup' : 'Operasional',
        'appName' : 'Tambah Data Dosen',
        'formDosen':formDosen,
        'pesan':pesan

    }
    return render(request,'olahDataDosen/create.html',context)
def delete(request,del_id):
    dosen.objects.filter(nik_id=del_id).delete()
    return redirect('olahDataDosen:index')

def update(request,update_id):
    dataDosen=dosen.objects.get(nik_id=update_id)
    dataFormDosen = {
        'nik_id':dataDosen.nik_id,
        'nidn':dataDosen.nidn,
        'jabatan':dataDosen.jabatan,
        'golongan':dataDosen.golongan,
    }
    formDosen = dosenForm(request.POST or None,initial=dataFormDosen,instance=dataDosen)
    if request.method=='POST':
        if formDosen.is_valid():
            formDosen.save()
            return redirect('olahDataDosen:index')

    context={
        'appGroup' : 'Operasional',
        'appName' : 'Ubah Data Dosen',
        'formDosen':formDosen
    }
    return render(request,'olahDataDosen/create.html',context)
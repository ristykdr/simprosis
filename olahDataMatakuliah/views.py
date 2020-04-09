from django.shortcuts import render, redirect
from . models import matakuliah
from django.http import HttpResponse
from .forms import matakuliahForm

# Create your views here.

def index (request):
    data_mk = matakuliah.objects.all()
    # print (data_mk)
    context = {
        'appGroup':'Operasional',
        'appName':'Olah Data Matakuliah',
        'datamk':data_mk,
    }
    return render(request,'olahDataMatakuliah/index.html',context)

def link(request,inputan):
    getlink = inputan
    return HttpResponse(getlink)

def create(request):
    print('ini create bro')
    mk_form=matakuliahForm(request.POST or None)
    if request.method=='POST':
        if mk_form.is_valid():
            mk_form.save()
            return redirect('olahDataMatakuliah:index')
    context={
        'appGroup':'Operasional',
        'appName':'Tambah Matakuliah',
        'mk_form':mk_form
    }
    return render(request,'olahDataMatakuliah/create.html',context)

def delete(request,del_id):
    matakuliah.objects.get(id=del_id).delete()
    return redirect('olahDataMatakuliah:index')

def update(request,update_id):
    data_mk=matakuliah.objects.get(id=update_id)
    dataMatakuliah = {
        'kode':data_mk.kode,
        'nama':data_mk.nama,
        'sks':data_mk.sks,
        'semester':data_mk.semester,
        'jmlPertemuan':data_mk.jmlPertemuan,
        'rumpunMatakuliah':data_mk.rumpunMatakuliah
    }
    mk_form=matakuliahForm(request.POST or None,initial=dataMatakuliah, instance=data_mk)
    if request.method=='POST':
        if mk_form.is_valid():
            mk_form.save()
            return redirect('olahDataMatakuliah:index')
    context={
        'appGroup':'Operasional',
        'appName':'Ubah Matakuliah',
        'mk_form':mk_form
    }
    return render(request,'olahDataMatakuliah/create.html',context)
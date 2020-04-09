from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from olahDataDosen.models import dosen
from rps.models import userProfiles
from . forms import dosenForm

def index(request):
    pengguna=request.user.username
    id_user=id_user = User.objects.get(username=pengguna).id
    id_profile=userProfiles.objects.get(namaUser_id=id_user).id
    id_dosen = dosen.objects.get(nik_id=id_profile).id

    print (id_dosen)
    dataDosen=dosen.objects.get(id=id_dosen)
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
            return redirect('biodataDosen:index')

    context={
        'appGroup' : 'Dosen',
        'appName' : 'Biodata Dosen',
        'formDosen':formDosen
    }
    return render(request,'biodataDosen/index.html',context)
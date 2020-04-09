from django.shortcuts import render
from django.contrib.auth.models import User
from olahDataMahasiswa.models import mahasiswa
from rps.models import userProfiles
# import form

# Create your views here.
def index(request) :
    context = {
        'appGroup' : 'Mahasiswa',
        'appName' : 'Biodata Mahasiswa',
    }
    return render (request,'biodataMahasiswa/index.html',context)
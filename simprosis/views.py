from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    context ={
        'appGroup':'Home',
        'appName':'isi Sementara',
        'nav':[
            ['/','Home'],
            ['rps/','RPS'],
        ],
        'banner':'',#img/icon_unp_trans.png
    }
    return render(request,'index.html',context)

def index2(request):
    return HttpResponse("<h1>INI INDEX</h1>")

def tes(request):
    return HttpResponse("ini tes")
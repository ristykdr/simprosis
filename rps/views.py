#views RPS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  . models import userProfiles, fakultas
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from . forms import userForm, userProfilesForm, prodiFormset
from django.contrib import messages



class fakultasListView(ListView):
    model = fakultas


class fakultasCreateView(CreateView):
    model = fakultas
    fields = [
        'namaFakultas'
    ]


class fakProdiCreateView(CreateView):
    model = fakultas
    fields=['namaFakultas']
    success_url = reverse_lazy('rps:fakultasList')

    def get_context_data(self, **kwargs):
        data = super(fakProdiCreateView,self).get_context_data(**kwargs)
        # context[""] = 
        if self.request.POST:
            data['programStudi']=prodiFormset(self.request.POST)
        else:
            data['programStudi']=prodiFormset()
        return data
    

    def form_valid(self, form):
        context=self.get_context_data()
        programStudi=context['programStudi']
        with transaction.atomic():
            self.object=form.save()
            if programStudi.is_valid():
                programStudi.instance=self.object
                programStudi.save()
        return super(fakProdiCreateView,self).form_valid(form)


class fakultasUpdateView(UpdateView):
    model = fakultas
    success_url = reverse_lazy('rps:fakultasList')
    fields=['namaFakultas']



class fakProdiUpdateView(UpdateView):
    model = fakultas
    fields=['namaFakultas']
    success_url = reverse_lazy('rps:fakultasList')

    def get_context_data(self, **kwargs):
        data = super(fakProdiUpdateView,self).get_context_data(**kwargs)
        if self.request.POST :
            data['programStudi']=prodiFormset(self.request.POST, instance=self.object)
        else:
            data['programStudi']=prodiFormset(instance=self.object)
        return data
    

    def form_valid(self, form):
        context=self.get_context_data()
        programStudi=context['programStudi']
        with transaction.atomic():
            self.object=form.save()
            
            if programStudi.is_valid():
                programStudi.instance=self.object
                programStudi.save()
        return super(fakProdiUpdateView,self).form_valid(form)



class fakultasDeleteView(DeleteView):
    model = fakultas
    success_url = reverse_lazy('rps:fakultasList')



# Create your views here.
def index(request): #index dari rps
    context = {
        'appGroup':'Olah Data RPS',
        'appName':'subjudul home rps',
        'nav':[
            ['/','Home'],
            ['','RPS'],
        ],
        'subnav':[
            ['submenurps/','Sub-menu RPS'],
            ['#','mennu 2'],
            ['#','menu3']
        ],
        'banner':'',
        'css_app':'rps/css/styles.css',
    }
    return render(request,'rps/index.html',context)


def dataFakultas():
    pass

def createFakultas():
    pass


def submenurps(request):
    context={
        'judul':'submenu RPS',
        'subjudul':'subjudul submenu rps',
    }
    return render(request,'index.html',context)

@login_required
@transaction.atomic
def profile(request):
    pesan = None
    pengguna=request.user.username
    # print('BROOOOO')
    # print(pengguna)
    data_user = User.objects.get(username=pengguna)
    id_pengguna=data_user.id
    dataFormUser = {
        'first_name': data_user.first_name,
        'last_name':data_user.last_name,
        'email':data_user.email,
    }
    print(id_pengguna)
    data_profile = userProfiles.objects.get(namaUser_id=id_pengguna)
    dataFormProfile = {
        # 'namaUser':data_profile.namaUser,
        'noKTP':data_profile.noKTP,
        'nama':data_profile.nama,
        'alamat':data_profile.alamat,
        'tanggalLahir':data_profile.tanggalLahir,
        'jenisKelamin':data_profile.jenisKelamin,
        'agama':data_profile.agama,
    }
    user_form = userForm(request.POST or None, initial=dataFormUser, instance=data_user)
    profile_form = userProfilesForm(request.POST or None, initial=dataFormProfile, instance=data_profile)
    if request.method=='POST' :
        if user_form.is_valid:
            user_form.save()
            if profile_form.is_valid:
                profile_form.save()
            else:
                pesan='Form Profil tidak valid'
        else:
            pesan='Form user tidak valid'
            
        return redirect('rps:profile')
    
    context ={
        'appGroup':'User Profiles',
        'appName':'Detail User : '+data_user.username,
        'user_form': user_form,
        'profile_form': profile_form,
        'pesan':pesan
    }
    return render(request,'rps/profile.html',context)



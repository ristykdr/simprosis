from django.shortcuts import render, redirect
from .forms import mahasiswaForm
from .models import mahasiswa
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from django.core.exceptions import ObjectDoesNotExist
import openpyxl

# from tablib import Dataset
# from .resources import mahasiswaResource

# Create your views here.


class mahasiswaCreateView(CreateView):
    form_class = mahasiswaForm
    template_name = 'olahDataMahasiswa/create.html'
    extra_context = {
        'appGroup':'Operasional',
        'appName': 'Olah Data Mahasiswa',
    }
    def get_context_data(self,*args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        # print(kwargs)
        return super().get_context_data(*args, **kwargs)


class mahasiswaUpdateView(UpdateView):
    model = mahasiswa
    form_class = mahasiswaForm
    template_name = 'olahDataMahasiswa/create.html'
    extra_context = {
        'appGroup':'Operasional',
        'appName': 'Olah Data Mahasiswa',
    }
    def get_context_data(self,*args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        # print(kwargs)
        return super().get_context_data(*args, **kwargs)



class mahasiswaListView(ListView):
    model = mahasiswa
    template_name = 'olahDataMahasiswa/index.html'
    ordering =['npm']
    paginate_by = 10
    extra_context = {
        'appGroup':'Operasional',
        'appName': 'Olah Data Mahasiswa',
    }
    def get_context_data(self,*args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        # print(kwargs)
        return super().get_context_data(*args, **kwargs)



class mahasiswaDeleteView(DeleteView):
    model = mahasiswa
    extra_context = {
        'appGroup':'Operasional',
        'appName': 'Olah Data Mahasiswa',
    }
    def get_context_data(self,*args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        # print(kwargs)
        return super().get_context_data(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('olahDataMahasiswa:index')



# def importDataMhs(request):
#     if request.method=='POST':
#         mahasiswa_resource = mahasiswaResource()
#         dataset = Dataset()
#         data_mhs_import = request.FILES['fileImport']

#         imported_data = dataset.load(data_mhs_import.read().decode('utf-8'),format='csv')
#         result = mahasiswa_resource.import_data(dataset, dry_run=True)

#         print(result.has_errors())
#         print(imported_data)

#         if not result.has_errors():
#             mahasiswa_resource.import_data(dataset, dry_run=False)
#     context = {
#         'appGroup':'Operasional',
#         'appName': 'Import Data Mahasiswa',
#         }
#     return render (request,'olahDataMahasiswa/importmhs.html',context)


def importDataMhs (request):
    context = {
            'appGroup': 'Operasional',
            'appName': 'Import Data Mahasiswa',
        }
    if request.method=='GET':
        
        return render (request,'olahDataMahasiswa/importmhs.html',context)
    
    else:
        data_mhs_import = request.FILES['fileImport']
        wb = openpyxl.load_workbook(data_mhs_import)
        # mendapatkan nama sheet
        worksheet = wb['Sheet1']
        print(worksheet)

        exel_data = list()
        dataSudahAda = list()
        # perulangan untuk baca row
        for row in worksheet.iter_rows(min_row=2, max_col=2):
            row_data = list()
            # perulangan untuk baca kolom
            for cell in row:
                isi = str(cell.value)
                row_data.append(isi.replace("'",""))
            # cek, create data di sini
            dataNpm = row_data[0]
            dataNama = row_data[1]
            try:
                mahasiswa.objects.get(npm=dataNpm)
                dataSudahAda.append(row_data)
                # pass
            except ObjectDoesNotExist:
                mahasiswa.objects.create(npm=dataNpm, nama=dataNama)
                exel_data.append(row_data)

            # print(row_data)
            # print('=======')
            # exel_data.append(row_data)
            
        context = {
            'appGroup': 'Operasional',
            'appName': 'Import Data Mahasiswa',
            
        }
        context['exel_data']=exel_data
        context['dataSudahAda']=dataSudahAda
        # print(exel_data)
        # print('----------------------------')
        # print(dataSudahAda)
        # print(context)
        return render (request,'olahDataMahasiswa/importmhs.html',context)




def index (request) :
    semua_mahasiswa = mahasiswa.objects.all()
    # print(semua_mahasiswa)
    context = {
        'appGroup':'Operasional',
        'appName': 'Olah Data Mahasiswa',
        'semua_mahasiswa':semua_mahasiswa
    }
    return render (request,'olahDataMahasiswa/index.html',context)

def create(request):
    formMahasiswa = mahasiswaForm(request.POST or None)
    # formMahasiswa.fields['nik'].queryset = userProfiles.objects.exclude(
    #     id__in=dosen.objects.all().values_list('nik_id',flat=True)
    # )
    if request.method=='POST':
        if formMahasiswa.is_valid():
            formMahasiswa.save()
            return redirect('olahDataMahasiswa:index')
    context = {
        'appGroup':'Operasional',
        'appName': 'Tambah Data Mahasiswa',
        'formMahasiswa':formMahasiswa
    }
    return render(request,'olahDataMahasiswa/create.html',context)

def delete(request,del_id):
    mahasiswa.objects.get(id=del_id).delete()
    return redirect('olahDataMahasiswa:index')

def update(request,update_id):
    dataMahasiswa = mahasiswa.objects.get(id=update_id)
    # formMahasiswa.fields['nik'].queryset = userProfiles.objects.exclude(
    #     id__in=dosen.objects.all().values_list('nik_id',flat=True)
    # )
    dataFormMahasiswa = {
        'nik':dataMahasiswa.nik,
        'npm':dataMahasiswa.npm,
        'tahunMasuk':dataMahasiswa.tahunMasuk,
        'kelas':dataMahasiswa.kelas
    }
    formMahasiswa = mahasiswaForm(request.POST or None, initial=dataFormMahasiswa, instance=dataMahasiswa)
    if request.method=='POST':
        if formMahasiswa.is_valid():
            formMahasiswa.save()
            return redirect('olahDataMahasiswa:index')
    context = {
        'appGroup':'Operasional',
        'appName': 'Tambah Data Mahasiswa',
        'formMahasiswa':formMahasiswa
    }
    return render(request,'olahDataMahasiswa/create.html',context)

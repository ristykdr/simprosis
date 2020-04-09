from django import forms
from django.forms import ModelForm
from olahDataJurnalKuliah.models import detilJurnalKuliah

class detilJurnalKuliahForm(forms.ModelForm):
    
    class Meta:
        model = detilJurnalKuliah
        fields = [
            'jurnal',
            'pertemuan',
            'tanggal',
            'jamMulai',
            'jamSelesai',
            'materi',
            'metode',
        ]
        labels = {
            'jurnal':'Jurnal Kuliah',
            'pertemuan':'Pertemuan',
            'tanggal':'Tanggal',
            'jamMulai':'Jam Mulai',
            'jamSelesai':'Jam Selesai',
            'materi':'Materi',
            'metode':'Metode Pembelajaran',
        }
        widgets ={
            'jurnal':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pertemuan':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Pertemuan ke - '
                }
            ),
            'tanggal':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'date'
                }
            ),
            'jamMulai':forms.TimeInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'time'
                }
            ),
            'jamSelesai':forms.TimeInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'time'
                }
            ),
            'materi':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    
                }
            ),
            'metode':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Metode Pembelajaran'
                }
            ),
        }

class updatedetilJurnalKuliahForm(forms.ModelForm):
    
    class Meta:
        model = detilJurnalKuliah
        fields = [
            'pertemuan',
            'tanggal',
            'jamMulai',
            'jamSelesai',
            'materi',
            'metode',
        ]
        labels = {
            'pertemuan':'Pertemuan',
            'tanggal':'Tanggal',
            'jamMulai':'Jam Mulai',
            'jamSelesai':'Jam Selesai',
            'materi':'Materi',
            'metode':'Metode Pembelajaran',
        }
        widgets ={
            'pertemuan':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Pertemuan ke - '
                }
            ),
            'tanggal':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'date'
                }
            ),
            'jamMulai':forms.TimeInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'time'
                }
            ),
            'jamSelesai':forms.TimeInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'time'
                }
            ),
            'materi':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    
                }
            ),
            'metode':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Metode Pembelajaran'
                }
            ),
        }
from django import forms
from django.forms import ModelForm, inlineformset_factory
from . models import jurnalKuliah, detilJurnalKuliah

class jurnalKuliahForm(forms.ModelForm):
    """Form definition for jurnalKuliah."""

    class Meta:
        """Meta definition for jurnalKuliahform."""

        model = jurnalKuliah
        fields = [
            'mk',
            'tahunAjaran',
            'semester',
            'dosenPengajar',
            'ruang',
            'pjmk',
            'kelas'
        ]
        labels ={
            'mk':'Matakuliah',
            'tahunAjaran':'Tahun Ajaran',
            'semester':'Semester',
            'dosenPengajar':'Dosen Pengampu',
            'ruang':'Ruang Kuliah',
            'pjmk':'PJMK',
            'kelas':'Kelas'
        }
        widgets = {
            'mk':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'tahunAjaran':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'semester':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'dosenPengajar':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'ruang':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Ruang Kelas'
                }
            ),
            'pjmk':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'PJMK'
                }
            ),
            'kelas':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Kelas'
                }
            )
        }


class detilJurnalKuliahForm(forms.ModelForm):
    """Form definition for detilJurnalKuliah."""

    class Meta:
        """Meta definition for detilJurnalKuliahform."""

        model = detilJurnalKuliah
        exclude=()
        # fields = [
        #     'jurnal',
        #     'pertemuan',
        #     'tanggal',
        #     'jamMulai',
        #     'jamSelesai',
        #     'materi',
        #     'metode'
        # ]
        labels ={
            'jurnal':'Jurnal',
            'pertemuan':'Pertemuan',
            'tanggal':'Tanggal Kuliah',
            'jamMulai':'Jam Mulai',
            'jamSelesai':'Jam Selesai',
            'materi':'Materi',
            'metode':'Metode'
        }
        widgets = {
            'jurnal':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pertemuan':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'tanggal':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'date'
                }
            ),
            'jamMulai':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'time'
                }
            ),
            'jamSelesai':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'time'
                }
            ),
            'materi':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Materi'
                }
            ),
            'metode':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Metode Belajar'
                }
            )
        }

JurnalFormset = inlineformset_factory(jurnalKuliah,detilJurnalKuliah,form=detilJurnalKuliahForm,extra=1)
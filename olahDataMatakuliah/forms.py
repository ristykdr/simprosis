from django import forms
from .models import matakuliah
class matakuliahForm(forms.ModelForm):
    
    class Meta:
        model = matakuliah
        fields = [
            'kode',
            'nama',
            'sks',
            'semester',
            'jmlPertemuan',
            'rumpunMatakuliah'
        ]
        labels = {
            'kode':'Kode Matakuliah',
            'nama':'Nama Matakuliah',
            'sks':'SKS',
            'semester':'Semester',
            'jmlPertemuan':'Jumlah Pertemuan',
            'rumpunMatakuliah':'Rumpun Matakuliah'
        }

        widgets = {
            'kode':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan kode matakuliah'
                }
            ),
            'nama':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan nama matakuliah'
                }
            ),
            'sks':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'SKS'
                }
            ),
            'semester':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'jmlPertemuan':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Jumlah pertemuan dalam satu semester'
                }
            ),
            'rumpunMatakuliah':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Rumpun Matakuliah'
                }
            )
        }

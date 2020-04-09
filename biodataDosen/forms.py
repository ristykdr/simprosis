from django import forms
from olahDataDosen.models import dosen
from django.forms import ValidationError

class dosenForm(forms.ModelForm):
    class Meta:
        model = dosen
        fields = [
            'nik',
            'nidn',
            'jabatan',
            'golongan'
        ]
        labels ={
            'nik':'Pilih user sebagai dosen',
            'nidn':'NIDN',
            'jabatan':'Jabatan',
            'golongan':'Golongan' 
        }
        widgets = {
            'nik':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan NIK',
                    'readonly':'True',
                    # 'disabled':'True'
                },

            ),
            'nidn':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Nomor Induk Dosen Nasional'
                }
            ),
            'jabatan':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
            'golongan':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                }
            )
        }
 
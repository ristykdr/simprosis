from django import forms
from . models import mahasiswa

class mahasiswaForm(forms.ModelForm):

    class Meta:

        model = mahasiswa
        fields = [
            'npm',
            'tahunMasuk',
            'kelas',

            'noKTP',
            'nama',
            'alamat',
            'tanggalLahir',
            'jenisKelamin',
            'agama'
        ]
        labels = {
            'npm':'Nomor Induk/Pokok Mahasiswa',
            'tahunMasuk':'Tahun Masuk mahasiswa',
            'kelas':'Kelas',

            'noKTP':'Nomor KTP',
            'nama':'Nama Lengkap',
            'alamat':'Alamat KTP',
            'tanggalLahir':'Tanggal Lahir',
            'jenisKelamin':'Jenis Kelamin',
            'agama':'Agama'
        }
        widgets = {
            'npm':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Contoh : xx.xx.xx.xxxx'
                }
            ),
            'tahunMasuk':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Tahun masuk',
                    # 'type':'date'
                }
            ),
            'kelas':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'kelas : "A", "B", ...'
                }
            ),

            'noKTP':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan Nomor KTP'
                }
            ),
            'nama':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan Nama Lengkap'
                }
            ),
            'alamat':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan alamat Sesuai KTP'
                }
            ),
            'tanggalLahir':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'date'
                }
            ),
            'jenisKelamin':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
            'agama':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                }
            )
        }


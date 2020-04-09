from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import rps, referensi, rps, detilRPS
from tinymce.widgets import TinyMCE


class rpsForm(forms.ModelForm):
    
    class Meta:
        model = rps
        fields = [
            'kodemk',
            'dosenPengampu',
            'capaianPembelajaran',
            'prasyarat',
            'pathLokasi',
            'deskripsi',

            'tanggalPenyusunan',
            'capaianPembelajaranProdi',
            'materiPembelajaran',
            'mediaBelajar',
            'teamTeaching',
            # 'idref'
        ]
        labels = {
            'kodemk':'Matakuliah',
            'dosenPengampu':'Dosen Pengampu',
            'capaianPembelajaran':'Capaian Pembelajaran',
            'prasyarat':'Matakuliah Prasyarat',
            'pathLokasi':'File',
            'deskripsi':'Deskripsi',

            'tanggalPenyusunan': 'Tanggal Penyusunan',
            'capaianPembelajaranProdi':'Capaian Pembelajaran Program Studi',
            'materiPembelajaran':'Materi Pembelajaran',
            'mediaBelajar':'Media Belajar',
            'teamTeaching':'Dosen Team Teaching',
            # 'idref':'Referensi'
        }

        widgets = {
            'kodemk':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Pilih Matakuliah'
                }
            ),
            'dosenPengampu':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Pilih Dosen Pengampu'
                }
            ),
            'capaianPembelajaran':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'prasyarat':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pathLokasi':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'File Path'
                }
            ),
            'deskripsi':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),

            'tanggalPenyusunan':forms.DateInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'type':'date'
                }
            ),
            'capaianPembelajaranProdi':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'materiPembelajaran':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'mediaBelajar':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'teamTeaching':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),

        }

class referensiForm(forms.ModelForm):
    
    class Meta:
        model = referensi
        fields = [
            'refRps',
            'jenis',
            'tipe',
            'judul',
            'author',
            'tahun',
            'kota',
            'penerbit',
        ]
        labels={
            'refRps':'Matakuliah',
            'jenis':'Jenis Referensi',
            'tipe':'Tipe',
            'judul':'Judul',
            'author':'Author',
            'tahun':'Tahun Terbit',
            'kota':'Kota',
            'penerbit':'Penerbit',
        }
        widgets={
            'refRps':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'jenis':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                    
                }
            ),
            'tipe':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'JeniS : Buku, Jurnal dll'
                }
            ),
            'judul':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Judul pustaka'
                }
            ),
            'author':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Author / Pengarang'
                }
            ),
            'tahun':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
            'kota':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Kota Terbit'
                }
            ),
            'penerbit':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Penerbit'
                }
            ),
        }


class detilRPSForm(forms.ModelForm):
    class Meta:
        model = detilRPS
        fields = [
            'idRps',
            'pertemuan',
            'kemampuan',
            'materiBelajar',
            'bentukMetodeBelajar',
            'pengalamanBelajarOffline',
            'pengalamanBelajarOnlineSinkron',
            'pengalamanBelajarOnlineAsinkron',
            'teknikPenilaian',
            'kriteriaPenilaian',
            'indikatorPenilaian',
            'bobotPenilaian',
        ]
        labels = {
            'idRps':'RPS',
            'pertemuan':'Pertemuan',
            'kemampuan':'Kemampuan',
            'materiBelajar':'Materi Pembelajaran',
            'bentukMetodeBelajar':'Metode Pembelajaran',
            'pengalamanBelajarOffline':'Pengalaman Belajar Offline',
            'pengalamanBelajarOnlineSinkron':'Pengalaman Belajar Online Sinkron',
            'pengalamanBelajarOnlineAsinkron':'Pengalaman Belajar Online Asinkron',
            'teknikPenilaian':'Teknik Penilaian',
            'kriteriaPenilaian':'Kriteria Penilaian',
            'indikatorPenilaian':'Indikator Penilaian',
            'bobotPenilaian':'Bobot Penilaian',
        }
        widgets = {
            'idRps':forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pertemuan':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
            'kemampuan':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    
                }
            ),
            'materiBelajar':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'bentukMetodeBelajar':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pengalamanBelajarOffline':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pengalamanBelajarOnlineSinkron':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pengalamanBelajarOnlineAsinkron':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'teknikPenilaian':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Teknik Penilaian'
                }
            ),
            'kriteriaPenilaian':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Kriteria Penilaian'
                }
            ),
            'indikatorPenilaian':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Indikator Penilaian'
                }
            ),
            'bobotPenilaian':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
        }

class detilRPSUpdateForm(forms.ModelForm):
    class Meta:
        model = detilRPS
        fields = [
            # 'idRps',
            'pertemuan',
            'kemampuan',
            'materiBelajar',
            'bentukMetodeBelajar',
            'pengalamanBelajarOffline',
            'pengalamanBelajarOnlineSinkron',
            'pengalamanBelajarOnlineAsinkron',
            'teknikPenilaian',
            'kriteriaPenilaian',
            'indikatorPenilaian',
            'bobotPenilaian',
        ]
        labels = {
            # 'idRps':'RPS',
            'pertemuan':'Pertemuan',
            'kemampuan':'Kemampuan',
            'materiBelajar':'Materi Pembelajaran',
            'bentukMetodeBelajar':'Metode Pembelajaran',
            'pengalamanBelajarOffline':'Pengalaman Belajar Offline',
            'pengalamanBelajarOnlineSinkron':'Pengalaman Belajar Online Sinkron',
            'pengalamanBelajarOnlineAsinkron':'Pengalaman Belajar Online Asinkron',
            'teknikPenilaian':'Teknik Penilaian',
            'kriteriaPenilaian':'Kriteria Penilaian',
            'indikatorPenilaian':'Indikator Penilaian',
            'bobotPenilaian':'Bobot Penilaian',
        }
        widgets = {
            # 'idRps':forms.Select(
            #     attrs={
            #         'class':'form-control form-control-sm'
            #     }
            # ),
            'pertemuan':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
            'kemampuan':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm',
                    
                }
            ),
            'materiBelajar':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'bentukMetodeBelajar':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pengalamanBelajarOffline':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pengalamanBelajarOnlineSinkron':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'pengalamanBelajarOnlineAsinkron':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'teknikPenilaian':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Teknik Penilaian'
                }
            ),
            'kriteriaPenilaian':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Kriteria Penilaian'
                }
            ),
            'indikatorPenilaian':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Indikator Penilaian'
                }
            ),
            'bobotPenilaian':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                }
            ),
        }

# rpsFormSet = inlineformset_factory(rps,referensi)
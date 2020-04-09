from django import forms
from . models import dosen
from django.forms import ValidationError

class dosenForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super (dosenForm,self).__init__(*args, **kwargs)
    #     for field in self.Meta.fields:
    #         self.fields[field].required=True
    
    # def clean_nik(self):
    #     nik_input = self.cleaned_data["nik"]

    #     if dosen.objects.filter(nik=nik_input).exists():
    #         raise ValidationError('nikd dobel')
    #         self.add_error('nik_input','kedobelan')
    #     return nik_input
    
    # def save(self):
    #     nik=self.cleaned_data.get('nik')
    #     nidn = self.cleaned_data.get('nidn')
    #     jabatan = self.cleaned_data.get('jabatan')
    #     golongan= self.cleaned_data.get('golongan')

    #     return dosen.objects.create(
    #         nik=nik,
    #         nidn=nidn,
    #         jabatan=jabatan,
    #         golongan=golongan
    #     )

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
            'nik':forms.Select(
                attrs={
                    'class':'form-control form-control-sm',
                    'placeholder':'Masukkan NIK'
                }
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
    
# def clean_nik(self):
#     data = self.cleaned_data["nik"]
#     if data:
#         if dosen.objects.filter(nik_id=1).exists():
#             raise forms.ValidationError('data sudah ada')
#     return data

        
    # def clean_nik_id(self,nik_id):
    #     # input_nik_id = self.cleaned_data.get('nik_id')
    #     if dosen.objects.filter(nik_id=1).exists():
    #     # if input_nik_id==1:
    #         raise forms.ValidationError('Dosen  sudah ada')
    #     # return input_nik_id
    #     return nik_id
    # def clean(self):
    #     data = self.cleaned_data
    #     if dosen.objects.filter(nik_id=1).exists():
    #         raise forms.ValidationError('sudah ada')

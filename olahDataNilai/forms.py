from django import forms
from django.forms import ModelForm
from presensiKuliah.models import presensi

class updateNilaiPresensiForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(updateNilaiPresensiForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['npm'].widget.attrs['readonly'] = True

    # def clean_npm(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.npm
    #     else:
    #         return self.cleaned_data['npm']
    class Meta:

        model = presensi
        fields = [
            # 'npm',
            'presensi',
            'presenceDate',
            'nilai'
        ]
        labels ={
            # 'npm':'Nama',
            'presensi':'Hadir',
            'presenceDate':'Waktu Hadir',
            'nilai':'Nilai'
        }
        widgets = {
            # 'npm':forms.Select(
            #     attrs={
            #         'class':'form-control form-control-sm',
            #         'readonly':'readonly',
            #         # 'disabled':'disabled'
            #     }
                
            # ),
            'presensi':forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'readonly':'readonly'
                }
                
            ),
            'presenceDate':forms.DateTimeInput(
                attrs={
                    'class':'form-control form-control-sm',
                    'readonly':'readonly'
                }
            ),
            'nilai':forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm',
                }
            )
        }
    
    

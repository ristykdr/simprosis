from django.core.exceptions import ValidationError
from .models import dosen

def validasi_nik(value):
    input_nik=value
    
    if dosen.objects.filter(nik_id=1).exists():
        pesanError = 'Dosen '+input_nik+' sudah ada, silahkan pilih yang lain'
        raise ValidationError (message)
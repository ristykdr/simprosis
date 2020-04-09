from django.db import models
from rps.models import userProfiles
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# def validasi_nik(value):
#     input_nik=value
#     if dosen.objects.filter(nik_id=input_nik).exists() ==True:
#         pesanError = 'Dosen '+str(input_nik)+' sudah ada, silahkan pilih yang lain'
#         raise ValidationError (pesanError)

# Create your models here.
class dosen(models.Model):
    list_jabatan = (
        ('Tenaga Pengajar','Tenaga Pengajar'),
        ('Asisten Ahli','Asisten Ahli'),
        ('Lektor','Lektor'),
        ('Lektor Kepala','Lektor Kepala'),
        ('Guru Besar','Guru Besar')
    )
    list_golongan=(
        ('3a','III/a'),
        ('3b','III/b'),
        ('3c','III/c'),
        ('3d','III/d'),
        ('4a','IV/a'),
        ('4b','IV/b'),
        ('4c','IV/c'),
        ('4d','IV/d'),
        ('4e','IV/e'),
    )
    nik = models.OneToOneField(
            userProfiles, 
            on_delete=models.CASCADE,
            unique=True,
            # validators = [validasi_nik]
        )
    nidn = models.CharField( max_length=10,unique=True)
    jabatan = models.CharField(max_length=50, choices=list_jabatan)
    golongan = models.CharField(max_length=5,choices=list_golongan)

    

    class Meta:
        verbose_name = "dosen"
        verbose_name_plural ="dosen"
        ordering =['-nik']
      
    def __str__(self):
        return "{}".format(self.nik.nama)

    # def get_absolute_url(self):
    #     return reverse("dosen_detail", kwargs={"pk": self.pk})

    
from django.db import models
from django.urls import reverse_lazy
from rps.models import userProfiles
from datetime import datetime
# Create your models here.
class mahasiswa(models.Model):
    listTahunMasuk = []
    for r in range((datetime.now().year-7),(datetime.now().year+1)):
        listTahunMasuk.append((r,r))
    # nik = models.OneToOneField(
    #     userProfiles, 
    #     on_delete=models.CASCADE, 
    #     unique=True,)
    npm = models.CharField(max_length=20,unique=True)
    tahunMasuk = models.IntegerField(choices=listTahunMasuk, blank=True, null=True)
    kelas = models.CharField(max_length=2, blank=True, null=True)
    
    list_agama = (
        ('islam','Islam'),
        ('katolik','Katolik'),
        ('kristen','Kristen'),
        ('hindu','Hindu'),
        ('budha','Budha'),
        ('konghucu','Konghucu')
    )
    list_kelamin = (
        ('Laki','Laki - Laki'),
        ('perempuan','Perempuan')
    )
    noKTP = models.IntegerField(null=True,blank=True)
    nama = models.CharField(max_length=50, null=True,blank=True)
    alamat = models.TextField(default='',null=True,blank=True)
    tanggalLahir = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    jenisKelamin = models.CharField(max_length=10, choices=list_kelamin,null=True,blank=True)
    agama = models.CharField(max_length=50,choices=list_agama,null=True,blank=True)

    class Meta:
        verbose_name = "mahasiswa"
        verbose_name_plural = "mahasiswa"

    def __str__(self):
        return "{} - {}".format(self.npm, self.nama)

    def get_absolute_url(self):
        return reverse_lazy('olahDataMahasiswa:index')

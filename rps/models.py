from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from olahDataMahasiswa.models import mahasiswa
# from olahDataMatakuliah.models import matakuliah

# Create your models here.
class fakultas(models.Model):
    namaFakultas = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'fakultas'
        verbose_name_plural = 'fakultas'
        ordering = ['-id']

    def __str__(self):
        return "{}".format(self.namaFakultas)

class prodi(models.Model):
    fak=models.ForeignKey(fakultas, on_delete=models.CASCADE)
    namaProdi = models.CharField(max_length=50)

    class Meta:
        """Meta definition for prodi."""

        verbose_name = 'prodi'
        verbose_name_plural = 'prodi'
        ordering = ['-id']

    def __str__(self):
        return "{}".format(self.namaProdi)


class userProfiles(models.Model):
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
    namaUser = models.OneToOneField(User, on_delete=models.CASCADE)
    noKTP = models.IntegerField(null=True,blank=True)
    nama = models.CharField(max_length=50, null=True,blank=True)
    alamat = models.TextField(default='',null=True,blank=True)
    tanggalLahir = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    jenisKelamin = models.CharField(max_length=10, choices=list_kelamin,null=True,blank=True)
    agama = models.CharField(max_length=50,choices=list_agama,null=True,blank=True)
    programStudi = models.ForeignKey(prodi, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.namaUser, self.nama)




# class krs(models.Model):
#     semAktif = models.CharField(max_length=50)
#     npm = models.ForeignKey(mahasiswa, on_delete=models.CASCADE)
#     matakuliah = models.ForeignKey(matakuliah, on_delete=models.CASCADE)

#     # TODO: Define fields here

#     class Meta:

#         verbose_name = 'krs'
#         verbose_name_plural = 'krss'
#         ordering =['-id']

#     def __str__(self):
#         return "{} - {}".format(self.id, self.npm)

    

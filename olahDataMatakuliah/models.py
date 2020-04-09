from django.db import models
from rps.models import prodi

# Create your models here.
class matakuliah(models.Model):
    list_semester=(
        (1,'Satu'),
        (2,'Dua'),
        (3,'Tiga'),
        (4,'Empat'),
        (5,'Lima'),
        (6,'Enam'),
        (7,'Tujuh'),
        (8,'Delapan')
    )
    kode = models.CharField(max_length=10,unique=True)
    nama = models.CharField(max_length=30)
    sks = models.IntegerField()
    semester = models.IntegerField(choices=list_semester)
    jmlPertemuan = models.SmallIntegerField(default=0)
    programStudi = models.ForeignKey(prodi, on_delete=models.CASCADE, blank=True, null=True)
    rumpunMatakuliah = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "matakuliah"
        verbose_name_plural = "matakuliah"
        ordering = ['-id']

    def __str__(self):
        return "{} - {}".format(self.kode,self.nama) 
    

        

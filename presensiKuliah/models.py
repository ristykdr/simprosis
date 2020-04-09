from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
# from olahDataMatakuliah.models import matakuliah
from olahDataMahasiswa.models import mahasiswa
from olahDataJurnalKuliah.models import detilJurnalKuliah

# Create your models here.
class presensi(models.Model):
    """Model definition for presensi."""
    # ambil dari detil jurnal
    # ambil dari mahasiswa
    # TODO: Define fields here
    jurnalPerkuliahan = models.ForeignKey(detilJurnalKuliah, on_delete=models.CASCADE, null=True)
    npm = models.ForeignKey(mahasiswa, on_delete=models.CASCADE)
    presensi = models.BooleanField(default=False)
    importDate = models.DateTimeField(auto_now_add=True)
    presenceDate =models.DateTimeField(blank=True, null=True)
    nilai = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    class Meta:
        """Meta definition for presensi."""

        verbose_name = 'presensi'
        verbose_name_plural = 'presensi'

    def __str__(self):
        return "{}-{}".format(self.jurnalPerkuliahan, self.npm)
    
    # def get_absolute_url(self):
    #     return reverse('olahDataNilai:nilaiperpertemuan', kwargs={
    #         "pk": self.jurnalPerkuliahan.id.id,
    #         "id_dtJurnal":self.jurnalPerkuliahan.id
    #         })
    
    # def save(self):
    #     pass

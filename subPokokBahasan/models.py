from django.db import models
from olahDataMahasiswa.models import mahasiswa
from olahDataJurnalKuliah.models import detilJurnalKuliah

# Create your models here.
# class presensi(models.Model):
#     """Model definition for presensi."""
#     # ambil dari detil jurnal
#     # ambil dari mahasiswa
#     # TODO: Define fields here
#     jurnalPerkuliahan = models.ForeignKey(detilJurnalKuliah, on_delete=models.CASCADE, null=True)
#     npm = models.ForeignKey(mahasiswa, on_delete=models.CASCADE)
#     presensi = models.BooleanField(default=False)

#     class Meta:
#         """Meta definition for presensi."""

#         verbose_name = 'presensi'
#         verbose_name_plural = 'presensi'

#     def __str__(self):
#         return "{}-{}".format(self.jurnalPerkuliahan, self.npm)
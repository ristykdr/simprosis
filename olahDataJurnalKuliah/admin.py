from django.contrib import admin
from .models import jurnalKuliah,detilJurnalKuliah, pesertaKuliah

# Register your models here.
admin.site.register(jurnalKuliah)
admin.site.register(detilJurnalKuliah)
admin.site.register(pesertaKuliah)
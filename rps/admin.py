from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.userProfiles)
admin.site.register(models.fakultas)
admin.site.register(models.prodi)
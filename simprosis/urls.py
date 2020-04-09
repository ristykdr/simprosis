"""simprosis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^rps/',include('rps.urls',namespace='rps')), #menghubungkan url rps dengan url project simprosis
    re_path(r'^biodataDosen/',include('biodataDosen.urls',namespace='biodataDosen')),
    re_path(r'^biodataMahasiswa/',include('biodataMahasiswa.urls',namespace='biodataMahasiswa')),
    re_path(r'^inputKRS/',include('inputKRS.urls',namespace='inputKRS')),
    re_path(r'^olahDataDosen/',include('olahDataDosen.urls', namespace='olahDataDosen')),
    re_path(r'^olahDataJurnalKuliah/',include('olahDataJurnalKuliah.urls',namespace='olahDataJurnalKuliah')),
    re_path(r'^olahDataMahasiswa/',include('olahDataMahasiswa.urls',namespace='olahDataMahasiswa')),
    re_path(r'^olahDataMatakuliah/',include('olahDataMatakuliah.urls',namespace='olahDataMatakuliah')),
    re_path(r'^olahDataNilai/',include('olahDataNilai.urls',namespace='olahDataNilai')),
    re_path(r'^olahDataRPS/',include('olahDataRPS.urls',namespace='olahDataRPS')),
    re_path(r'^presensiKuliah/',include('presensiKuliah.urls',namespace='presensiKuliah')),
    re_path(r'^rekapHasilKuliah/',include('rekapHasilKuliah.urls',namespace='rekapHasilKuliah')),
    re_path(r'^rekapKRS/',include('rekapKRS.urls',namespace='rekapKRS')),
    re_path(r'^rekapPresensi/',include('rekapPresensi.urls', namespace='rekapPresensi')),
    re_path(r'^rekapRPS/',include('rekapRPS.urls',namespace='rekapRPS')),
    re_path(r'^subPokokBahasan/',include('subPokokBahasan.urls',namespace='subPokokBahasan')),
    re_path(r'^tes/$',views.tes),
    re_path(r'^tinymce/', include('tinymce.urls')),
    path('',views.index, name='index')
]

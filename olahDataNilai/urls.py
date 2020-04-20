from django.urls import path, re_path, include
from django.conf.urls import url
from . views import (
    jurnalKuliahListView,
    jurnalKuliahDetailView,
    nilaiPerPertemuan,
    nilaiUpdateView,
    exportNilaiHarian,
    importNilaiHarian,
    rekapTotalDetailView,
    exportNilaiAkhir
)

app_name='olahDataNilai'
urlpatterns = [
    # re_path(r'^$',views.index, name='index'),
    re_path(r'^$',jurnalKuliahListView.as_view(),name='index'),
    re_path(r'^(?P<pk>[0-9]+)$',jurnalKuliahDetailView.as_view(),name='detiljurnalkuliah'),
    re_path(r'^rekapTotal/(?P<pk>[0-9]+)$',rekapTotalDetailView.as_view(),name='rekapTotal'),
    re_path(r'^nilaiperpertemuan/(?P<pk>[0-9]+)/(?P<id_dtJurnal>[0-9]+)$',nilaiPerPertemuan.as_view(),name='nilaiperpertemuan'),
    re_path(r'^nilaiUpdateView/(?P<idJurnal>[0-9]+)/(?P<id_dtJurnal>[0-9]+)/(?P<pk>[0-9]+)$',nilaiUpdateView.as_view(),name='nilaiUpdateView'),
    re_path(r'^exportNilaiHarian/(?P<jurnalPerkuliahan>[0-9]+)$',exportNilaiHarian,name='exportNilaiHarian'),
    re_path(r'^importNilaiHarian/(?P<idJurnal>[0-9]+)/(?P<id_dtJurnal>[0-9]+)$',importNilaiHarian,name='importNilaiHarian'),
    re_path(r'^exportNilaiAkhir/(?P<idJurnal>[0-9]+)$',exportNilaiAkhir,name='exportNilaiAkhir'),
]

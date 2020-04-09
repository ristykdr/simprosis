from django.urls import path, re_path, include
from django.conf.urls import url
from . views import (
    jurnalKuliahListView,
    jurnalKuliahDetailView,
    nilaiPerPertemuan,
    nilaiUpdateView,
    exportNilaiHarian
)

app_name='olahDataNilai'
urlpatterns = [
    # re_path(r'^$',views.index, name='index'),
    re_path(r'^$',jurnalKuliahListView.as_view(),name='index'),
    re_path(r'^(?P<pk>[0-9]+)$',jurnalKuliahDetailView.as_view(),name='detiljurnalkuliah'),
    re_path(r'^nilaiperpertemuan/(?P<pk>[0-9]+)/(?P<id_dtJurnal>[0-9]+)$',nilaiPerPertemuan.as_view(),name='nilaiperpertemuan'),
    re_path(r'^nilaiUpdateView/(?P<idJurnal>[0-9]+)/(?P<id_dtJurnal>[0-9]+)/(?P<pk>[0-9]+)$',nilaiUpdateView.as_view(),name='nilaiUpdateView'),
    re_path(r'^exportNilaiHarian/(?P<jurnalPerkuliahan>[0-9]+)$',exportNilaiHarian,name='exportNilaiHarian'),
]

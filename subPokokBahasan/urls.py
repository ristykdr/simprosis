from django.urls import path, re_path, include
from django.conf.urls import url
from . views import (
    jurnalKuliahListView, 
    jurnalKuliahDetailView,
    detilJurnalKuliahCreateView,
    detilJurnalKuliahFromRPSCreateView,
    detilJurnalKuliahUpdateView,
    detilJurnalKuliahDeleteView,
    detilRPSListView,
    presensiDetailView,
    importPesertaKuliah,
    buatPresensi
)

app_name='subPokokBahasan'
urlpatterns = [
    # tambahkan url presensi ke app presensiKuliah
    re_path(r'^$', jurnalKuliahListView.as_view(),name='index'),
    re_path(r'^presensi/(?P<pk>[0-9]+)/(?P<id_dtJurnal>[0-9]+)$',presensiDetailView.as_view(),name='presensi'),
    re_path(r'^presensi/buatPresensi/(?P<idJurnal>[0-9]+)/(?P<id_dtJurnal>[0-9]+)$',buatPresensi, name='buatPresensi'),
    re_path(r'^presensi/importPesertaKuliah/(?P<id_dtjurnal>[0-9]+)$',importPesertaKuliah,name='importPesertaKuliah'),
    re_path(r'^(?P<pk>[0-9]+)$',jurnalKuliahDetailView.as_view(), name='detiljurnalkuliah'),
    re_path(r'^createdetiljurnalfromrps/(?P<id_jurnal>[0-9]+)/(?P<id_rps>[0-9]+)$',detilJurnalKuliahFromRPSCreateView.as_view(),name='createdetiljurnalfromrps'),
    re_path(r'^createdetiljurnal/(?P<id_jurnal>[0-9]+)$',detilJurnalKuliahCreateView.as_view(),name='createdetiljurnal'),
    re_path(r'^detiljurnalfromrps/(?P<id_rps>[0-9]+)/(?P<id_jurnal>[0-9]+)$',detilRPSListView.as_view(),name='detiljurnalfromrps'),
    re_path(r'^updatedetiljurnal/(?P<pk>[0-9]+)$',detilJurnalKuliahUpdateView.as_view(),name='updatedetiljurnal'),
    re_path(r'^deletedetiljurnal/(?P<pk>[0-9]+)$',detilJurnalKuliahDeleteView.as_view(),name='deletedetiljurnal'),

]

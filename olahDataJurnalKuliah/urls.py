from django.urls import path, re_path, include
from django.conf.urls import url
from . views import (
    jurnalKuliahListView,
    jurnalKuliahCreateView,
    jurnalPerkuliahanCreateView,
    jurnalPerkuliahanUpdateView,
    jurnalKuliahDeleteView,
    jurnalKuliahDetailView,
    importPesertaKuliah
)

app_name='olahDataJurnalKuliah'
urlpatterns = [
    re_path(r'^$',jurnalKuliahListView.as_view(),name='jurnalKuliahList'),
    re_path(r'^createjurnal/$',jurnalKuliahCreateView.as_view(),name='jurnal-add'),
    re_path(r'^updatejurnal/(?P<pk>[0-9]+)$',jurnalPerkuliahanUpdateView.as_view(),name='jurnal-update'),
    re_path(r'^deletejurnal/(?P<pk>[0-9]+)$',jurnalKuliahDeleteView.as_view(),name='jurnal-delete'),
    re_path(r'^detailjurnal/(?P<pk>[0-9]+)$',jurnalKuliahDetailView.as_view(),name='detailjurnal'),
    re_path(r'^importPesertaKuliah/(?P<idJurnal>[0-9]+)$',importPesertaKuliah, name='importPesertaKuliah'),
]

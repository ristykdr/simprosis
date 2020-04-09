from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.generic import ListView
from .views import(
    index,createrps,deleterps, updaterps,
    # createreferensi,
    referensiCreateView, referensiUpdateView, referensiDeleteView,
    rpsListView, rpsDetailView,detilRPSCreateView, detilRPSUpdateView, detilRPSDeleteView
) 

app_name='olahDataRPS'
urlpatterns = [
    re_path(r'^$',rpsListView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)$',rpsDetailView.as_view(),name='detailrps'),
    re_path(r'^updatedetailrps/(?P<pk>[0-9]+)$', detilRPSUpdateView.as_view(),name='detilRPSUpdateView'),
    re_path(r'^createdetailrps/(?P<id_rps>[0-9]+)$',detilRPSCreateView.as_view(),name='createdetailrps'),
    re_path(r'^deletedetilrps/(?P<pk>[0-9]+)$', detilRPSDeleteView.as_view(), name='deletedetilrps'),
    re_path(r'^createreferensi/(?P<id_rps>[0-9]+)$',referensiCreateView.as_view(), name='createreferensi'),
    re_path(r'^updatereferensi/(?P<pk>[0-9]+)$',referensiUpdateView.as_view(),name='updatereferensi'),
    re_path(r'^deletereferensi/(?P<pk>[0-9]+)$',referensiDeleteView.as_view(),name='deletereferensi'),
    # (?P<id_rps>[0-9]+)
    # re_path(r'^$',index, name='index'),
    re_path(r'^createrps/$',createrps, name='createrps'),
    re_path(r'^deleterps/(?P<del_id>[0-9]+)$',deleterps, name='deleterps'),
    re_path(r'^updaterps/(?P<update_id>[0-9]+)$',updaterps, name='updaterps'),
    
    # re_path(r'^createreferensi$',createreferensi, name='createreferensi')
]

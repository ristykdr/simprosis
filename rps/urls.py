#urls RPS
from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name='rps'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^submenurps/$',views.submenurps),
    re_path(r'^profile/$',views.profile,name='profile'),
    path('fakultas/',views.fakultasListView.as_view(),name='fakultasList'),
    re_path(r'^updatefakultas/(?P<pk>[0-9]+)$',views.fakProdiUpdateView.as_view(),name='fakultas-update'),
    re_path(r'^deletefakultas/(?P<pk>[0-9]+)$',views.fakultasDeleteView.as_view(),name='fakultas-delete'),
    re_path(r'^createfakultas$',views.fakProdiCreateView.as_view(),name='fakultas-add')
]

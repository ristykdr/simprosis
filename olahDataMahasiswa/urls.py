from django.urls import path, re_path, include
from django.conf.urls import url
from .views import (
    mahasiswaCreateView,
    mahasiswaUpdateView,
    mahasiswaListView,
    mahasiswaDeleteView,
    importDataMhs
)

app_name='olahDataMahasiswa'
urlpatterns = [
    re_path(r'^$',mahasiswaListView.as_view(),name='index'),
    re_path(r'^import$',importDataMhs, name='import'),
    re_path(r'^create/$',mahasiswaCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>[0-9]+)$',mahasiswaUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>[0-9]+)$',mahasiswaDeleteView.as_view(),name='delete')
]

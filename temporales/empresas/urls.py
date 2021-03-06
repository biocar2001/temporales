from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^empresas/$', views.indexEmpresas, name='empresas'),
    url(r'^newEmpresa/$', views.new_empresa, name='newEmpresa'),
    url(r'^newOferta/(?P<idempresa>\d+)/$', views.new_oferta, name='newOferta'),
    url(r'^detailEmpresa/(?P<idempresa>\d+)/$', views.detailEmpresa, name='detailEmpresa'),
    url(r'^detailOferta/(?P<idoferta>\d+)/(?P<idempresa>\d+)/$', views.detailOferta, name='detailOferta'),
]
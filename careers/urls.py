from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^acreditation/model/national', views.viewNational, name='national'),
    url(r'^acreditation/arcusur', views.viewArcusur, name='arcusur'),
    url(r'^acreditation/posgrado', views.viewPosgrado, name='postgrado'),
    url(r'^acreditation/postponed', views.viewPostponed, name='postponed'),
    url(r'^acreditation/no-reputable', views.viewNoReputable, name='noreputable'),
    url(r'^acreditation/render-pdf', views.renderPdf, name='renderPdf'),
]
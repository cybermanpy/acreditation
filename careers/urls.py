from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^acreditation/model/national', views.viewNational, name='national'),
    url(r'^acreditation/career', views.viewCareer, name='career'),
    url(r'^acreditation/university', views.viewUniversity, name='university'),
    url(r'^acreditation/postponed', views.viewPostponed, name='postponed'),
    url(r'^acreditation/no-reputable', views.viewNoReputable, name='noreputable'),
]
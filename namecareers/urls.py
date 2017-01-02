from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard/evaluator/career/list/$', views.viewNameCareer, name='list'),
    url(r'^dashboard/evaluator/career/new/$', views.newNameCareer, name='new'),
    url(r'^dashboard/evaluator/career/edit/(?P<pk>[0-9]+)/$', views.editNameCareer, name='edit'),
]
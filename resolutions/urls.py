from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard/evaluator/resolution/view/$', views.viewResolution, name='view'),
    url(r'^dashboard/evaluator/resolution/new/$', views.ResolutionCreate.as_view(), name='new'),
    url(r'^dashboard/evaluator/resolution/list/$', views.ResolutionList.as_view(), name='list'),
    url(r'^dashboard/evaluator/resolution/edit/(?P<pk>\d+)$', views.ResolutionEdit.as_view(), name='edit'),
]
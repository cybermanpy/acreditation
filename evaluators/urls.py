from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard/evaluator/institutional/$', views.viewEvaluatorInstitutional, name='institutional'),
    url(r'^dashboard/evaluator/degree/$', views.viewEvaluatorDegree, name='degree'),
    url(r'^dashboard/evaluator/list/$', views.viewEvaluator, name='evaluator'),
    url(r'^dashboard/evaluator/add/new/$', views.newEvaluator, name='new'),
    url(r'^dashboard/evaluator/edit/(?P<pk>[0-9]+)/$', views.editEvaluator, name='edit'),
    # url(r'^dashboard/evaluator/add/type/$', views.newTypeEvaluator, name='newtype'),
    url(r'^dashboard/evaluator/edit/type/(?P<pk>[0-9]+)/$', views.editTypeEvaluator, name='editType'),
    url(r'^dashboard/evaluator/list/institutional/$', views.searchInstitutional, name='searchInstitutional'),
    url(r'^dashboard/evaluator/list/degree/$', views.searchDegree, name='searchDegree'),
    url(r'^dashboard/evaluator/cleanner/(?P<link>\w+)/$', views.cleanner, name='cleanner'),
    url(r'^dashboard/evaluator/list/view/$', views.EvaluatorList.as_view(), name='list'),
    url(r'^dashboard/evaluator/add/type/(?P<label>[0-9]+)/(?P<user>[0-9]+)$', views.newEvaluatorInstitutional, name='addType'),
    # url(r'^dashboard/evaluator/list/institutional/$', views.ListInstitutional.as_view(), name='listInstitutional'),
    url(r'^dashboard/evaluator/list/agronomia/$', views.ListAgronomia.as_view(), name='listAgronomia'),
    url(r'^dashboard/evaluator/(?P<pk>[0-9]+)/$', views.EvaluatorDetail.as_view(), name='EvaluatorDetail'),
]
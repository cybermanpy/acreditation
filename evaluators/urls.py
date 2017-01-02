from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard/evaluator/institucional/$', views.viewEvaluatorInstitutional, name='institutional'),
    url(r'^dashboard/evaluator/grado/$', views.viewEvaluatorGrado, name='grado'),
    url(r'^dashboard/evaluator/list/$', views.viewEvaluator, name='evaluator'),
    url(r'^dashboard/evaluator/add/new/$', views.newEvaluator, name='new'),
    url(r'^dashboard/evaluator/edit/(?P<pk>[0-9]+)/$', views.editEvaluator, name='edit'),
    url(r'^dashboard/evaluator/add/type/$', views.newTypeEvaluator, name='newtype'),
    url(r'^dashboard/evaluator/edit/type/(?P<pk>[0-9]+)/$', views.editTypeEvaluator, name='editType'),
    url(r'^dashboard/evaluator/list/view/$', views.EvaluatorList.as_view(), name='list'),
    url(r'^dashboard/evaluator/(?P<pk>[0-9]+)/$', views.EvaluatorDetail.as_view(), name='EvaluatorDetail'),
]
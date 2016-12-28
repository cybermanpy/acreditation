from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^acreditation/evaluators', views.viewEvaluator, name='evaluator'),
    # url(r'^acreditation/evaluators/$', views.viewEvaluator, name='evaluator'),
    url(r'^acreditation/evaluatorList', views.EvaluatorList.as_view(), name='EvaluatorList'),
    url(r'^acreditation/evaluator/(?P<pk>[0-9]+)/$', views.EvaluatorDetail.as_view(), name='EvaluatorDetail'),
]
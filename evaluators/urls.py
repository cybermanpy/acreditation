from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^acreditation/evaluators', views.viewEvaluator, name='evaluator'),
]
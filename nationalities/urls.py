from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard/evaluator/nationality/view/$', views.viewNationality, name='view'),
    url(r'^dashboard/evaluator/nationality/new/$', views.NationalityCreate.as_view(), name='new'),
    url(r'^dashboard/evaluator/nationality/edit/(?P<pk>\d+)$', views.NationalityEdit.as_view(), name='edit'),
]
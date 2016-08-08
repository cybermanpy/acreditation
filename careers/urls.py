from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^acreditation/views', views.viewCareers, name='careers'),
]
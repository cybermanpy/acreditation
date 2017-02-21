from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^acreditation/model/national/$', views.viewNational, name='national'),
    url(r'^acreditation/model/arcusur/$', views.viewArcusur, name='arcusur'),
    url(r'^acreditation/posgrado/$', views.viewPosgrado, name='postgrado'),
    url(r'^acreditation/postponed/$', views.viewPostponed, name='postponed'),
    url(r'^acreditation/no-reputable/$', views.viewNoReputable, name='noreputable'),
    url(r'^acreditation/history/$', views.viewHistory, name='history'),
    url(r'^acreditation/pdfnational/$', views.pdfNational, name='pdfNational'),
    url(r'^acreditation/pdfarcusur/$', views.pdfArcusur, name='pdfArcusur'),
    url(r'^acreditation/pdfpostponed/$', views.pdfPostponed, name='pdfPostponed'),
    url(r'^acreditation/pdfno-reputable/$', views.pdfNoReputable, name='pdfNoReputable'),
    url(r'^acreditation/pdfposgrado/$', views.pdfPosgrado, name='pdfPosgrado'),
    url(r'^acreditation/pdfhistory/$', views.pdfHistory, name='pdfHistory'),
    url(r'^acreditation/report/$', views.report, name='report'),
    url(r'^acreditation/cleanner/(?P<link>\w+)/$', views.cleanner, name='cleanner'),
    url(r'^acreditation/api/v1/$', views.careersJson, name='careersJson'),
    # url(r'^acreditation/v1/json/(?P<year>[0-9]+)/$', views.careersJson, name='careersJson'),
    # url(r'^acreditation/render-pdf/$', views.renderPdf, name='renderPdf'),
    # url(r'^acreditation/pdfnational/(?P<search>\w+[^/]+)/(?P<options>\w+)/$', views.pdfNational, name='pdfNational'),
    # url(r'^acreditation/pdfnational/(?P<search>\w+.+)/(?P<options>\w+)/$', views.pdfNational, name='pdfNational'),
    # url(r'^acreditation/pdfarcusur/(?P<search>\w+.+)/(?P<options>\w+)/$', views.pdfArcusur, name='pdfArcusur'),
]
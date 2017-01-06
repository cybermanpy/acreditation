from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('careers.urls', namespace='careers')),
    url(r'^', include('evaluators.urls', namespace='evaluators')),
    url(r'^', include('userprofiles.urls', namespace='userprofiles')),
    url(r'^', include('namecareers.urls', namespace='namecareers')),
    url(r'^', include('resolutions.urls', namespace='resolutions')),
    url(r'^', include('nationalities.urls', namespace='nationalities')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

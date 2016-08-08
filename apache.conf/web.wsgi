import os
import sys

path = '/var/www/html/acreditation'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'acreditation.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

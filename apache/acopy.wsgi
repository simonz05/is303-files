import os, sys, site

apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)

sys.path.append(workspace)
site.addsitedir('/home/acopy/django/trafo/ve/lib/python2.6/site-packages')
#sys.path.append('/usr/lib/python2.6/dist-packages/django')
sys.path.append('/home/acopy/django/trafo')

os.environ['DJANGO_SETTINGS_MODULE'] = 'trafo.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

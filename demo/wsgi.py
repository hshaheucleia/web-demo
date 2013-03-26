"""
WSGI config for demo_2 project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import django.core.handlers.wsgi

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'demo')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/ubuntu/eclweb/demo'
if path not in sys.path:
    sys.path.append(path)


# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

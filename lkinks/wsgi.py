"""
WSGI config for lkinks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
#PROJECT_PATH = "/home/ubuntu/lkinks"
PROJECT_PATH = "/var/www/lkinks"
import sys
if PROJECT_PATH not in sys.path:
   sys.path.append(PROJECT_PATH)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lkinks.settings")

application = get_wsgi_application()

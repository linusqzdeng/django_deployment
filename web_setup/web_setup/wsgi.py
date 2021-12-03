"""
WSGI config for web_setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from os.path import dirname, abspath

# Add project directory to sys.path
proj_dir = '/Users/linus/Nothinghere/django_setup/web_setup/polls'
if proj_dir not in sys.path:
    print(proj_dir)
    sys.path.append(proj_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_setup.settings')
application = get_wsgi_application()

PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

"""WSGI config for paper_search project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paper_search.settings")

application = get_wsgi_application()
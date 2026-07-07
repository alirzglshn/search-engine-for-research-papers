"""ASGI config for paper_search project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paper_search.settings")

application = get_asgi_application()
"""
Django settings for paper_search project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-change-this-key-for-any-real-deployment"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# When DEBUG=True, Django's runserver ignores ALLOWED_HOSTS entirely,
# so this list only matters in production. The "testserver" entry is used
# by Django's test client and can be removed before deploying.
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "papers",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "paper_search.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "paper_search.wsgi.application"


# Database
# No Django models back the search results (the inverted index is a pickle
# file loaded directly into memory). SQLite is kept only because Django
# requires a configured database to run management commands and the dev
# server cleanly.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Search engine integration
# Path to the pre-built inverted index pickle. Loaded once per process
# on first search via papers.services.index_loader.get_index().

SEARCH_INDEX_PATH = BASE_DIR / "data" / "indexes" / "inverted_index.pkl"

# Number of results shown per page on the search results page.
SEARCH_RESULTS_PER_PAGE = 10


STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"  
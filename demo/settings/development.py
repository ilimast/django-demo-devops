import os
from os import environ

from .base import *

DEBUG = True
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", default="unsafe-secret-key")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default=["localhost"])


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


INTERNAL_IPS = ["127.0.0.1:8000"]

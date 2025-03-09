import os

from .base import *

DEBUG = False
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# Cargar variables de entorno desde Kubernetes Secrets o Vault
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "postgres-service"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "example.com").split(",")
STATIC_URL = "/static/"
STATIC_ROOT = "/app/static/"

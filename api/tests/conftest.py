import os
import django
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings.development")
django.setup()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Permitir acceso a la base de datos en todas las pruebas sin decoradores."""
    pass

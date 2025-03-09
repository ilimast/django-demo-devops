import pytest
from api.models import User

@pytest.mark.django_db
def test_create_user():
    """Test para verificar que se puede crear un usuario correctamente."""
    user = User.objects.create(name="Test User", dni="12345678901")
    assert user.name == "Test User"
    assert user.dni == "12345678901"
    assert User.objects.count() == 1

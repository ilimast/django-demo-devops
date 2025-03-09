import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from api.models import User
from api.views import UserViewSet


@pytest.mark.django_db
def test_get_users_list():
    """Test para verificar que la vista devuelve una lista de usuarios."""
    User.objects.create(name="User1", dni="12345678901")
    User.objects.create(name="User2", dni="12345678902")

    factory = APIRequestFactory()
    request = factory.get(reverse("users-list"))
    view = UserViewSet.as_view({"get": "list"})
    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 2

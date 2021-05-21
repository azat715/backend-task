from datetime import date, time
import json

import pytest
from django.core.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer


from core.models import Address, AddressType, Order, Client
from core.serializers import ClientSerializer


from .conftest import content, client_get, client_get_json


@pytest.mark.django_db
def test_order():
    client = Client(
        firstname="Ivan",
        lastname="Ivanov",
        email="test@gmail.com",
        phone_number="7-111-11-11-21",
    )
    with pytest.raises(ValidationError):
        client.full_clean()
    client.phone_number = "8-111-111-11-11"
    client.save()
    assert client.firstname == "Ivan"
    assert client.lastname == "Ivanov"
    assert client.email == "test@gmail.com"
    assert client.phone_number == "8-111-111-11-11"
    address = Address(
        client=client,
        city="Самара",
        street="Мичурина",
        building="21",
        type_address=1558,
        number="501",
    )
    with pytest.raises(ValidationError):
        address.full_clean()
    address.type_address = AddressType.OFFICE
    address.save()

    dt = date(2021, 1, 1)  # pylint: disable=invalid-name
    t = time.fromisoformat("00:01:01")  # pylint: disable=invalid-name
    order = Order(
        client=client,
        bottle_count=1,
        date=dt,
        time=t,
    )
    order.save()


@pytest.mark.django_db
def test_fixture_db(content):
    clients = Order.objects.count()
    assert clients == 1


"тестирование serializers"


# @pytest.mark.django_db
# def test_serializer(content, client_get_json):
#     serializer = ClientSerializer(data=client_get_json)
#     print(serializer.initial_data)
#     status = serializer.is_valid()
#     assert status
#     try:
#         serializer.save()
#     except Exception as e:
#         pytest.fail("CatAndPostsSerializer произошла ошибка при save() \n {}".format(e))
#         pytest.fail(e)


@pytest.mark.django_db
def test_first_order(content, client_get):
    try:
        client = Client.objects.first()
        serializer = ClientSerializer(client)
        assert serializer.data == client_get
    except Exception as e:
        pytest.fail("ClientSerializer произошла ошибка при serialize \n {}".format(e))
        pytest.fail(e)

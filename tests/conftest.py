import json
from collections import OrderedDict
from datetime import date, time

import pytest

from core.models import Address, AddressType, Client, Order


@pytest.fixture(scope="session")
def content(django_db_setup, django_db_blocker):
    """
    заполение базы данных
    """
    with django_db_blocker.unblock():
        client = Client(
            firstname="Ivan",
            lastname="Ivanov",
            email="test@gmail.com",
            phone_number="8-111-111-11-11",
        )
        client.save()
        address = Address(
            client=client,
            city="Самара",
            street="Мичурина",
            building="21",
            type_address=AddressType.OFFICE,
            number="501",
        )
        address.save()
        order = Order(
            client=client,
            bottle_count=1,
            date=date(2021, 1, 1),
            time=time.fromisoformat("00:01:01"),
        )
        order.save()


@pytest.fixture
def client_get_json():
    return {
        "address": [
            {
                "city": "Самара",
                "street": "Мичурина",
                "building": "32",
                "type_address": 1,
                "number": "501",
                "client": 1,
            }
        ],
        "orders": [
            {
                "bottle_count": 2,
                "date": "2021-01-05",
                "time": "00:01:01",
                "client": 1,
            }
        ],
        "firstname": "Fedor",
        "lastname": "Ivanov",
        "email": "test@gmail.com",
        "phone_number": "8-111-111-11-12",
    }


@pytest.fixture
def client_get():
    return {
        "id": 1,
        "address": [
            OrderedDict(
                [
                    ("id", 1),
                    ("city", "Самара"),
                    ("street", "Мичурина"),
                    ("building", "21"),
                    ("type_address", 1),
                    ("number", "501"),
                    ("client", 1),
                ]
            )
        ],
        "orders": [
            OrderedDict(
                [
                    ("id", 1),
                    ("bottle_count", 1),
                    ("date", "2021-01-01"),
                    ("time", "00:01:01"),
                    ("client", 1),
                ]
            )
        ],
        "firstname": "Ivan",
        "lastname": "Ivanov",
        "email": "test@gmail.com",
        "phone_number": "8-111-111-11-11",
    }

from django.db import models

# Create your models here.

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from rest_framework import serializers

validate_phone = RegexValidator(
    regex=r"^8(?:-\d{3}){2}(?:-\d{2}){2}$",
    message="Номер телефона должен быть в формате 8-xxx-xxx-xx-xx",
)


class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(
        unique=True,
    )
    phone_number = models.CharField(
        validators=[validate_phone],
        max_length=25,
        unique=True,
    )

    def __repr__(self):
        return "Client({self.firstname}, {self.lastname}, {self.email}, {self.phone_number}".format(
            self=self
        )

    def __str__(self):
        return self.__repr__()


class AddressType(models.IntegerChoices):
    OFFICE = 1, "Office"
    APT = 2, "Apartment"


class Address(models.Model):
    client = models.ForeignKey(
        Client(), on_delete=models.CASCADE, related_name="address", blank=True
    )
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=95)
    building = models.CharField(max_length=10)
    type_address = models.SmallIntegerField(choices=AddressType.choices)
    number = models.CharField(max_length=20)

    def __repr__(self):
        return "Address({self.city}, {self.street}, {self.building}, {self.type_address}, {self.number})".format(
            self=self
        )

    def __str__(self):
        return self.__repr__()


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders", blank=True
    )
    bottle_count = models.PositiveSmallIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def clean(self):
        if self.date.isoweekday() in [1, 2, 3, 4, 5]:
            print("будни")
            if (
                10 > self.time.hour > 11
                or 12 > self.time.hour > 13
                or 15 > self.time.hour > 16
            ):
                pass
            else:
                raise serializers.ValidationError(
                    {"time": "Доставка по будням только 10-11:00, 12-13:00 и 15-16:00"}
                )
        elif self.date.weekday() in [6, 7]:
            if 12 > self.time.hour > 13 or 15 > self.time.hour > 16:
                pass
            else:
                raise serializers.ValidationError(
                    {"time": "Доставка по выходным только 12-13:00 и 15-16:00"}
                )

    def __repr__(self):
        return "Order({self.bottle_count}, {self.date}, {self.time}".format(self=self)

    def __str__(self):
        return self.__repr__()

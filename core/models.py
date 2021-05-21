from django.db import models

# Create your models here.

from django.core.validators import RegexValidator

validate_phone = RegexValidator(
    regex=r"/^8(?:-\d{3}){2}(?:-\d{2}){2}$/gm",
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
        max_length=15,
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
        Client(), on_delete=models.CASCADE, related_name="address"
    )
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=95)
    building = models.CharField(max_length=10)
    type_address = models.SmallIntegerField(choices=AddressType.choices)
    number = models.CharField(max_length=10)

    def __repr__(self):
        return "Address({self.city}, {self.street}, {self.building}, {self.type_address}, {self.number})".format(
            self=self
        )

    def __str__(self):
        return self.__repr__()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    bottle_count = models.PositiveSmallIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __repr__(self):
        return "Order({self.bottle_count}, {self.date}, {self.time}".format(self=self)

    def __str__(self):
        return self.__repr__()

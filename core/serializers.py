from rest_framework import serializers

from core.models import Order, Address, Client


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(
        many=True,
    )
    orders = OrderSerializer(
        many=True,
    )

    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        orders_data = validated_data.pop("orders")
        client = Client(**validated_data)
        for address_item in address_data:
            Address.objects.create(client=client, **address_item)
        for order in orders_data:
            Order.objects.create(client=client, **order)
        return client

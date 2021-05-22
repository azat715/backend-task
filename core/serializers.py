from rest_framework import serializers

from core.models import Order, Address, Client


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["bottle_count", "date", "time"]


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    orders = OrderSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        orders_data = validated_data.pop("orders")
        if not Client.objects.filter(
            phone_number=validated_data["phone_number"]
        ).exists():
            print("111")
            client = Client.objects.create(**validated_data)
        else:
            client = Client.objects.get(phone_number=validated_data["phone_number"])
        for address_item in address_data:
            Address.objects.create(client=client, **address_item)
        for order in orders_data:
            item = Order(client=client, **order)
            item.clean()
            item.save()
        return client

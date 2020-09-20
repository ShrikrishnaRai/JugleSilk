from rest_framework import serializers

from categories.models import Categories
from products.models import Product


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=1000)
    summary = serializers.CharField(default='Best quality Pashmina')
    colors = serializers.CharField(max_length=120)
    createdBy = serializers.CharField(default="John Doe")

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

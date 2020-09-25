from rest_framework import serializers

from productEnquiries.models import productEnquiries


class ProductEnquiriesSerializers(serializers.Serializer):
    email = serializers.EmailField()
    fullName = serializers.CharField()
    phoneNumber = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        return productEnquiries.objects.create(**validated_data)
from rest_framework import serializers

from quoterequest.models import QuoteRequest


class SerializerForQuoteRequest(serializers.Serializer):
    fullName = serializers.CharField()
    address = serializers.CharField()
    email = serializers.EmailField()
    phoneNo = serializers.CharField()
    categories = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return QuoteRequest.objects.create(**validated_data)

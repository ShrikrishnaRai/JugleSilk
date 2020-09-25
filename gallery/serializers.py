from rest_framework import serializers


class GallerySerializers(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField()
    uploadedBy = serializers.CharField()

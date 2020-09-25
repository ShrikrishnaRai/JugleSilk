from rest_framework import serializers


class SliderSerializers(serializers.Serializer):
    sliderImage = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField()

from rest_framework import serializers


class CategoriesSerializers(serializers.Serializer):
    categoriesIconImage = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField()
    summary = serializers.CharField()
    createdBy = serializers.CharField()

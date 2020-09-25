from rest_framework import serializers

from blogs.models import Blogs


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField()
    blogsImage = serializers.ImageField()

    def create(self, validated_data):
        return Blogs.objects.create(**validated_data)

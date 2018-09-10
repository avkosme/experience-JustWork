from rest_framework import serializers
from page.models import Page
from content.models import Video


class PageSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('id', 'detail_url',)

    def get_detail_url(self, obj):
        return '/'.join(('/page', str(obj.pk)))


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

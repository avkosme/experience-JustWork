from rest_framework import serializers
from page.models import Page


class PagesSerializer(serializers.ModelSerializer):
    VERSION = 'v1'
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('title', 'detail_url')

    def get_detail_url(self, obj):
        return '/'.join(('/api', self.VERSION, 'page', str(obj.slug), ''))


class PageSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('title', 'content')

    def get_content(self, obj):
        return obj.get_content()

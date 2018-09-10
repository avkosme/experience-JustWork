from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.queue import counter
from .serializers import PageSerializer
from page.models import Page as PageModel


class Page(generics.ListAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        return PageModel.objects.all()


class PageDetail(APIView):
    STATUS_OK = 'ok'
    STATUS_ERR = 'err'

    __slots__ = ('status', 'data', 'message')

    def __init__(self):
        super().__init__()
        self.status = []
        self.data = []
        self.message = ''

    def get(self, request, slug, format=None):
        try:
            page = PageModel.objects.get(slug=slug)
            list(counter.delay(type='video', pk=video.pk) for video in page.video_set.all())
            list(counter.delay(type='audio', pk=audio.pk) for audio in page.audio_set.all())
            list(counter.delay(type='text', pk=text.pk) for text in page.text_set.all())
        except PageModel.DoesNotExist:
            self.status = self.STATUS_ERR
            self.message = 'Страница не найдена'

        response = Response(
            {'status': self.status, 'data': self.data, 'message': self.message},
            status=status.HTTP_200_OK,
            content_type='application/json; charset=utf-8',
            headers={
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            }
        )

        return response

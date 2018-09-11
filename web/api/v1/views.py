from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.queue import counter
from .serializers import PageSerializer, PagesSerializer
from page.models import Page as PageModel

class Pages(generics.ListAPIView):
    serializer_class = PagesSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return PageModel.objects.all()


class PageDetail(APIView):
    STATUS_OK = 'ok'
    STATUS_ERR = 'err'

    __slots__ = ('status', 'data', 'message', 'response_data')

    def __init__(self):
        super().__init__()
        self.status = []
        self.data = []
        self.message = ''
        self.response_data = dict()

    def get(self, *args, **kwargs):
        try:
            page = PageModel.objects.get(slug=kwargs.get('slug'))
            page_serializer = PageSerializer(instance=page)
            self.data = page_serializer.data
            self.response_data = {'status': self.STATUS_OK, **self.data}

            list(counter.delay(type='video', pk=video.pk) for video in page.video_set.all())
            list(counter.delay(type='audio', pk=audio.pk) for audio in page.audio_set.all())
            list(counter.delay(type='text', pk=text.pk) for text in page.text_set.all())

        except PageModel.DoesNotExist:
            self.response_data = {'status': self.STATUS_ERR, 'message': 'Страница не найдена'}

        response = Response(
            self.response_data,
            status=status.HTTP_200_OK,
            content_type='application/json; charset=utf-8',
            headers={
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            }
        )

        return response

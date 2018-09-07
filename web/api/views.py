from rest_framework import generics
from page.models import Page as PageModel
from .serializers import PageSerializer


class Page(generics.ListAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        return PageModel.objects.all()

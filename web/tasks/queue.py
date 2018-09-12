import os
import django
from django.db.models import F
from celery import Celery, shared_task

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'core.settings.base'
)

django.setup()

app = Celery('tasks')
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)


@shared_task
def counter(**kwargs):
    from content.models import Video, Audio, Text
    if kwargs.get('type') == 'video':
        video, pk = Video.objects.get_or_create(pk=kwargs.get('pk'))
        video.counter = F('counter') + 1
        return video.save()
    if kwargs.get('type') == 'audio':
        audio, pk = Audio.objects.get_or_create(pk=kwargs.get('pk'))
        audio.counter = F('counter') + 1
        return audio.save()
    if kwargs.get('type') == 'text':
        text, pk = Text.objects.get_or_create(pk=kwargs.get('pk'))
        text.counter = F('counter') + 1
        return text.save()

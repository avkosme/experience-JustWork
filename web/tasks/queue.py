import os
import django
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
        video = Video.objects.get(pk=kwargs.get('pk'))
        video.counter = video.counter + 1
        return video.save()
    if kwargs.get('type') == 'audio':
        audio = Audio.objects.get(pk=kwargs.get('pk'))
        audio.counter = audio.counter + 1
        return audio.save()
    if kwargs.get('type') == 'text':
        text = Text.objects.get(pk=kwargs.get('pk'))
        text.counter = text.counter + 1
        return text.save()

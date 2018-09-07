from django.contrib import admin
from content.models import Video, Audio


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ['counter']
    search_fields = ['title']

class AudioAdmin(admin.ModelAdmin):
    readonly_fields = ['counter']
    search_fields = ['title']


admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)

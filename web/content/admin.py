from django.contrib import admin
from content.models import Video, Audio, Text


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ['counter']
    search_fields = ['title']


class AudioAdmin(admin.ModelAdmin):
    readonly_fields = ['counter']
    search_fields = ['title']


class TextAdmin(admin.ModelAdmin):
    readonly_fields = ['counter']
    search_fields = ['title']

    class Media:
        js = ('js/tinymce/tinymce.min.js', 'js/tinymce/tiny-init.js')


admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Text, TextAdmin)

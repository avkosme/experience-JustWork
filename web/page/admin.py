from django import forms
from django.contrib import admin
from page.models import Page
from content.models import Video, Audio, Text


class VideoInline(admin.StackedInline):
    model = Video
    extra = 0
    fields = ('title', 'url_file', 'counter')
    readonly_fields = ('counter',)
    verbose_name = 'Видео'


class AudioInline(admin.StackedInline):
    model = Audio
    extra = 0
    fields = ('title', 'url_file', 'counter')
    readonly_fields = ('counter',)
    verbose_name = 'Аудио'


class TextInline(admin.StackedInline):
    model = Text
    extra = 0
    fields = ('title', 'content', 'counter')
    readonly_fields = ('counter',)
    verbose_name = 'Текст'


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['title', 'status']
    search_fields = ['title', 'text__title', 'text__content']
    inlines = [TextInline, VideoInline, AudioInline]


admin.site.register(Page, PageAdmin)

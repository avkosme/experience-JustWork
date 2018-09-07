from django.contrib import admin
from page.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['title', 'status']
    search_fields = ['title']

admin.site.register(Page, PageAdmin)

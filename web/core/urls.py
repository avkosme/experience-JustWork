from django.contrib import admin
from django.urls import re_path, include
from api.v1.views import Pages, PageDetail

api_patterns = [
    re_path('^pages[/]?$', Pages.as_view(), name='pages'),
    re_path('(?P<slug>[0-9a-z.\-\[\]]+)[/]?$', PageDetail.as_view(), name='page_detail'),
]

urlpatterns = [
    re_path('admin[/]?', admin.site.urls),
    re_path('^api/(?P<version>(v1))/', include(api_patterns)),
]

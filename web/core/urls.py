from django.contrib import admin
from django.urls import path, re_path
from api.views import Page, PageDetail

urlpatterns = [
    path('', Page.as_view(), name='page'),
    path('admin/', admin.site.urls),
    re_path('(?P<slug>[0-9a-z.\-\[\]]+)[/]?$', PageDetail.as_view(), name='page_detail'),
]

from django.contrib import admin
from django.urls import path
from api.views import Page

urlpatterns = [
    path('', Page.as_view(), name='page'),
    path('admin/', admin.site.urls),
]

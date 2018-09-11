import json
from django.urls import reverse
from rest_framework.test import APITestCase
from page.models import Page
from django.test import TestCase


class PagesListAPIViewTestCase(APITestCase):
    """Список страниц"""
    version = 'v1'
    url = reverse("pages", args=(version,))

    def setUp(self):
        self.page = Page.objects.create(title="Тестовая страница")

    def test_list_pages(self):
        response = self.client.get(self.url)
        response_data = json.loads(response.content)

        test_response_data = {
            'count': 1, 'next': None, 'previous': None,
            'results': [{
                'title': 'Тестовая страница', 'detail_url': '/api/v1/page/testovaia-stranitsa/'
            }]}
        self.assertEqual(test_response_data, response_data)
        self.assertEqual(200, response.status_code)


class PageDetailAPIViewTestCase(APITestCase):
    """Детальная информация о странице"""
    version = 'v1'
    slug = 'testovaia-stranitsa'
    url = reverse("page_detail", args=(version, slug))

    def setUp(self):
        self.page = Page.objects.create(title="Тестовая страница")

    def test_list_pages(self):
        response = self.client.get(self.url)
        response_data = json.loads(response.content)

        test_response_data = {
            'status': 'ok', 'title': 'Тестовая страница',
            'content': {'video': [], 'audio': [], 'text': []}
        }
        self.assertEqual(test_response_data, response_data)
        self.assertEqual(200, response.status_code)


class PageCreateTestCase(TestCase):
    """Создание страниц без API"""

    def setUp(self):
        Page.objects.create(title="Тестовая страница")

    def test_page_create(self):
        page = Page.objects.get(title="Тестовая страница")
        self.assertEqual(page.title, 'Тестовая страница')

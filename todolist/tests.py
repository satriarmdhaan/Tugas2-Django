from django.test import TestCase, Client
from django.urls import resolve

class AppTest(TestCase):
    def test_app_url_html(self):
        response = Client().get('/todolist/')
        self.assertEqual(response.status_code,200)

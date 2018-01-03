from django.test import TestCase
from django.urls import resolve
from comics.views import system_page
from django.http import HttpRequest
from django.contrib.auth.models import User

# Create your tests here.
class SystemPageTest (TestCase):

    def test_system_page_url_resolves(self):
        found = resolve('/system/')
        self.assertEqual(found.func, system_page)

    def test_system_page_returns_correct_html(self):
        user = User(username='anonymous', email='anon@mail.ru', password='password')
        user.is_active = False        
        request = HttpRequest()
        request.user = user
        response = system_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>Comics</title>', response.content)



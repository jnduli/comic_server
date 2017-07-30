from django.test import TestCase
from django.core.urlresolvers import resolve
from comics.views import system_page
from django.http import HttpRequest

# Create your tests here.
class SystemPageTest (TestCase):

    def test_system_page_url_resolves(self):
        found = resolve('/comic/system/')
        self.assertEqual(found.func, system_page)

    def test_system_page_returns_correct_html(self):
        request = HttpRequest()
        response = system_page(request)
        self.assertTrue(response.content.startsWith(b'<html>'))
        self.assertIn('<title>Comic Site</title>', response.content)
        self.assertTrue(response.content.endsWith(b'</html>'))



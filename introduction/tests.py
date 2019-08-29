from django.test import TestCase
from .views import *
from django.http import HttpRequest, response
from django.urls import resolve
#from .urls import *

class Testcls(TestCase):
    def test_root_url_resolves_to_hoempage_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'intro:main') 

    def home_page_returns_correct_html(self):
        request = HttpRequest()
        response = MainTV(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>일정관리</title>', html)
        self.assertTrue(html.endswith('</html>'))


from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class IndexViewTest(TestCase):

    def test_get_response_from_slash_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_get_response_from_importer_page(self):
        response = self.client.get(reverse('importer:index'))
        self.assertEqual(response.status_code, 200)


from textwrap import dedent
import re
from django import test
from django.db.models import Model, CharField, TextField
from django.forms import Form, ModelForm
from multiselect import widgets, fields
from django.urls import reverse
from bs4 import BeautifulSoup

class ExampleAppTetsts(test.TestCase):

    @property
    def url(self):
        return reverse('index')

    def test_loads_example_app(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_can_select_item(self):
        response = self.client.get(self.url)
        soup = BeautifulSoup(response.content, features="html.parser")
        item = soup.findAll('option')
        print(item)
        self.assertIn('<option value="1">One</option>', str(item))
        self.assertIn('<option value="2">Two</option>', str(item))
        self.assertIn('<option value="3">Three</option>', str(item))
        self.assertIn('<option value="4">Four</option>', str(item))

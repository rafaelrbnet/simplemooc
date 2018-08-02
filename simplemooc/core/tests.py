from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class CoreViewTest(TestCase):

    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        client = Client()
        response = client.get(reverse('core:home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_contact_code(self):
        client = Client()
        response = client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_template_used(self):
        client = Client()
        response = client.get(reverse('core:contact'))
        self.assertTemplateUsed(response, 'contact.html')
        self.assertTemplateUsed(response, 'base.html')

from django.test import TestCase
from django.conf.urls import url

class AccountViewTest(TestCase):

    def test_template_response(self):
        response = self.client.get('/accounts/login')
        self.assertContains(response, "ok")

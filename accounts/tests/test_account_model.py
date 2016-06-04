from django.test import TestCase
from accounts.models import (UserManager, Account)

# Create your tests here.

class UserModelTest(TestCase):

    def test_create_user(self):
        email = "kakaxi@sohu.com"
        username = "kakaxi"
        u1 = Account.objects.create_user(email=email, username=username)
        u2 = Account.objects.get(email=email)
        self.assertEqual(u1, u2)




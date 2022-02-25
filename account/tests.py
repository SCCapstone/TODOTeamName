from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Profile

# Create your tests here.
"""
class AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',
                                                         password='testpassword',
                                                         email='testemail@email.com')
        self.account = Profile.objects.create(user= self.user, name = 'testname') 

    def tearDown(self):
        self.user.delete()
        self.account.delete()

    def test_name(self):
        self.assertEqual(self.account.username, 'testuser')
        self.assertEqual('testuser', 'testuser')"""

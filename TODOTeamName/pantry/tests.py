from django.test import TestCase
from .models import pantryItems 
import datetime

# Create your tests here.

class pantryTestCases(TestCase):
    def setUp(self):
        self.item = pantryItems.objects.create(name = 'bananas', expiration = datetime.date(2022, 2, 2))
        self.item2 = pantryItems.objects.create(name= 'apples', expiration = datetime.date(2022,2,3))
   # def tearDown(self):
   #     self.item.delete()
    def test_pantry_string(self):
        self.assertEqual(str(self.item), 'bananas (expires 2022-02-02)') 
        self.assertEqual(str(self.item2), 'apples (expires 2022-02-03)')
        self.item.delete()
        self.item2.delete()

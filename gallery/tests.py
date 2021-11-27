from django.test import TestCase
from .models import Location, Category

# Create your tests here.
class LocationTestCase(TestCase):
    def setUp(self):
        self.name = Location(name='London')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location))

class CategoryTestCase(TestCase):
    def setUp(self):
        self.name = Category(name='Beach')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))
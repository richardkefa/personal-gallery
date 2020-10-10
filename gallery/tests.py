from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):
  
  #setup method
  def setUp(self):
    self.mountain= Image(image_name='mountkenya',Image_description='The tallest mountain in kenya')
    
  #testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.mountain,Image))
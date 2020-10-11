from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):
  
  #setup method
  def setUp(self):
    self.mountain= Image(image_name='mountkenya',Image_description='The tallest mountain in kenya')
    self.mountain.save_image()
    
  #testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.mountain,Image))
    
  #Creating a new category sand saving it
  self.new_category = Category(category= 'test-category')
  self.new_category.save()
    
  #Creating a new location and saving it
  self.new_location = Location(location='test-location')
  self.new_location.save()
  
  def test_all_images(self):
    images = Image.all_images()
    self.assertTrue(len(images)>0)
    
  def tearDown(self):
    
    Image.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete(
from django.db import models

# Create your models here.
class Image(models.Model):
  image = models.CharField()
  image_name = models.CharField()
  Image_description = models.TextField()
  lodation = models.ForeignKey(Location)
  category = models.ForeignKey(Category)
  
  def __str__(self):
    return self.image
  
  def save_image(self):
    self.save()
  
  
class Location(models.Model):
  location = models.CharField(max_length=50)
  
class Category(models.Model):
  category = models.CharField()
  
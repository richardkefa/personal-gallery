from django.db import models

# Create your models here.
  
class Location(models.Model):
  location = models.CharField(max_length=50)
  
  def __str__(self):
    return self.location

class Category(models.Model):
  category = models.CharField(max_length=50)
  
  def __str__(self):
    return self.category
  


class Image(models.Model):
  image = models.ImageField(upload_to ='photo-album/')
  image_name = models.CharField(max_length=100)
  Image_description = models.TextField()
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.image_name
  
  def save_image(self):
    self.save()

  class Meta:
    ordering = ['image']
    
  @classmethod
  def all_images(cls):
    images = cls.objects.all()
    return images

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category

# Create your views here.
def all_photos(request):
  images = Image.all_images()
  return render(request, 'welcome.html',{"images":images})

def image(request,image_id):
  try:
    image = Image.objects.get(id=image_id)
  except DoesNotExist:
    raise Http404()
  return render(request, 'full-gallery/pic.html',{"image":image})


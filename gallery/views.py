from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def all_photos(request):
  images = Image.all_images()
  return render(request, 'welcome.html',{"images":images})

def image(request):
  return render(request, 'full-gallery/pic.html')
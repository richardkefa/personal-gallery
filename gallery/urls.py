from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$',views.all_photos,name='all_images'),
  url(r'^photo/(\d+)',views.image,name='single_photo'),
  url(r'^search/',views.search_results,name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

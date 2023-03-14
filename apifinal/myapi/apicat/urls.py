from django.urls import path
from .views import get_cat_images

urlpatterns = [
    path('cat-images/', get_cat_images, name='get_cat_images'),
]

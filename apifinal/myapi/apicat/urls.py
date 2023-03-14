from django.urls import path
from .views import get_cat_images

#Routes the url to the get_cat_images function in views.py

urlpatterns = [
    path('cat-images/', get_cat_images, name='get_cat_images'),
]

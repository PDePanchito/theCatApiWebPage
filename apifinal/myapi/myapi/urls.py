from django.contrib import admin
from django.urls import path, include
from apicat.views import get_cat_images

#Ignore this routes, they are not necessary for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('apicat.urls')),
    path('add/', include('apicat.urls')),
    path('cat-images/', get_cat_images, name='get_cat_images'), # New URL pattern for the get_cat_images view
]

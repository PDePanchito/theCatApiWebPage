from django.contrib import admin
from .models import Cat

#I needed this at the beginning because i was trying to use the admin panel to add data to a database 
#and then i realized it was not necessary to do so, my bad
admin.site.register(Cat)


from django.db import models

#Cat.models is the data that will be stored in the database
class Cat(models.Model):
    breed_name = models.CharField(max_length=40)
    cat_temperament = models.CharField(max_length=100)
    cat_origin = models.CharField(max_length=20)
    cat_description = models.CharField(max_length=300)
    cat_wikipedia = models.URLField(max_length=200)
    cat_image = models.URLField(max_length=200)
    
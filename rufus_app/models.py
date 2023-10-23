# Create your models here.
from django.db import models

class Menu(models.Model):
    image = models.ImageField(upload_to='staticfiles/rest_framework/img/', default='')
    

class DishItem(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

class Dish(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    plato = models.CharField(max_length=255, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes', default=None)
    dish_items = models.ManyToManyField(DishItem, related_name='dishes', blank=True)



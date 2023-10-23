from django.contrib import admin
from .models import Menu, Dish, DishItem

# Register your models here.
admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(DishItem)

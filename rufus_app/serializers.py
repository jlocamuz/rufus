from rest_framework import serializers
from .models import Menu, Dish, DishItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class DishItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishItem
        fields = '__all__'

from rest_framework import viewsets
from rest_framework.response import Response

from .utils.foto_a_texto import obtener_texto_imagen
from .models import Menu, Dish, DishItem
from .serializers import MenuSerializer, DishSerializer, DishItemSerializer
from .utils.dish_to_tag import get_closest_matches
from .utils.dish_to_tag import get_menu_items
from .utils.get_urls import get_urlss

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        instance_id = data.get('id')
        instance = Menu.objects.get(id=instance_id)
        nombres ,texto = obtener_texto_imagen(data)
        lista_menus = get_menu_items(nombres,texto, instance_id)
        dishes = Dish.objects.filter(menu=instance)
        lista_of_urls_perdish = get_urlss(dishes, lista_menus)
        print(lista_of_urls_perdish)
        return Response({'lista_of_urls_perdish': lista_of_urls_perdish})

    def list(self, request, *args, **kwargs):
        path_imagen = 'staticfiles/rest_framework/img/MENU_5XSjgIX.jpeg'

        return super().list(request, *args, **kwargs)
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishItemViewSet(viewsets.ModelViewSet):
    queryset = DishItem.objects.all()
    serializer_class = DishItemSerializer

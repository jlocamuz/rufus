from django.core import serializers
import json
import requests
from ..models import DishItem, Dish

def get_urlss(dishes, dicc):
    lista = []
    
    for dish in dishes:
        dish_obj = dish
        plato = eval(dish_obj.plato)
        dish_items = []
        
        for item in plato:
            dish_item = DishItem.objects.filter(name=item).first()
            
            if dish_item:
                url = dish_item.url
            else:
                id = dicc.get(item, {}).get('closest_match_id')
                
                if not id:
                    continue
                url = f'https://static.arasaac.org/pictograms/{id}/{id}_300.png'
                response = requests.get(url)
                print(response, 'response')
                
                if response.ok:
                    dish_item = DishItem.objects.create(name=item, url=url)
            
            dish_obj.dish_items.add(dish_item)
            dish_items.append(dish_item)
        
        dish_obj.save()
        dish_json = json.loads(serializers.serialize('json', [dish_obj]))[0]
        dish_item_jsons = []
        
        for dish_item in dish_items:
            dish_item_json = json.loads(serializers.serialize('json', [dish_item]))[0]
            dish_item_jsons.append(dish_item_json)
        
        dish_json['dish_items'] = dish_item_jsons
        lista.append(dish_json)
    
    return lista

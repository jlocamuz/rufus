from dish_to_tag import get_closest_matches
from dish_to_tag import get_menu_items
from foto_a_texto import obtener_texto_imagen
from get_urls import get_urlss
if __name__ == '__main__':
    path_imagen = '/Users/julialocamuz/Downloads/MENU.jpeg'
    texto_imagen = obtener_texto_imagen(path_imagen)
    d = get_menu_items(texto_imagen)
    lista_of_urls_perdish = get_urlss(texto_imagen, get_closest_matches(d))

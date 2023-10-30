import re
import pytesseract
import cv2
import requests

from .texto_a_ingred import procesar_oracion

def obtener_texto_imagen(menu_object):
    url_imagen = menu_object['image']
    url_imagen_sin_host = url_imagen.replace('http://192.168.1.42:8000/', '')
    
    img = cv2.imread(url_imagen_sin_host)
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Realizar la umbralización
    umbral = 128  # Ajusta este valor según tus necesidades
    _, img_expuesta = cv2.threshold(gray, umbral, 255, cv2.THRESH_BINARY)

    # Convertir la imagen de umbralización a RGB
    img_expuesta_rgb = cv2.cvtColor(img_expuesta, cv2.COLOR_GRAY2BGR)

    # Fusionar la imagen original y la imagen de umbralización
    img_fusionada = cv2.addWeighted(img, 0.5, img_expuesta_rgb, 0.5, 0)

    texto = pytesseract.image_to_string(img_fusionada, lang='spa')
    print(texto)
    oraciones = re.split(r'\$\d+', texto)
    texto = [linea.lower().replace('\n', '').rstrip() for linea in oraciones if linea.strip()]
    palabras_oraciones = []
    for oracion in texto:
        oracion = oracion.split('$')[0].strip()
        
        palabras_oraciones.append(procesar_oracion(oracion))
    #print("palabras oraciones ", palabras_oraciones)
    #[['milanesa de cerdo', 'papas fritas'], ['pancho', 'nuggets'], ['hamburguesa', 'fritas']]

    print('palabras oraciones',palabras_oraciones)
    return texto, palabras_oraciones
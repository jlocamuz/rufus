import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import cess_esp

# Asegúrate de descargar los recursos necesarios

nltk.download('punkt_tab')

# Etiquetas POS en español
etiquetas = ['NC', 'AQ', 'NP']  # Sustantivos comunes, adjetivos, nombres propios
exclusiones = ['$', '€', '£', '¥']

# función para procesar cada oración
def procesar_oracion(oracion):
    print('procesa oracion', oracion)
    palabras_seleccionadas = []
    tokens = word_tokenize(oracion, language='spanish')
    tagged = pos_tag(tokens, tagset='esp')

    j = 0
    while j < len(tagged):
        token, pos = tagged[j]
        if pos in etiquetas and token not in exclusiones:
            # Comprobar si hay un 'de' entre sustantivos
            if j + 1 < len(tagged) and tagged[j + 1][0] == 'de' and j + 2 < len(tagged) and tagged[j + 2][1] == 'NC':
                palabra = token + ' de ' + tagged[j + 2][0]
                # Unir si hay otro sustantivo después
                if j + 3 < len(tagged) and tagged[j + 3][1] == 'NC':
                    palabra += ' ' + tagged[j + 3][0]
                    j += 1
                palabras_seleccionadas.append(palabra)
                j += 2 
            elif j + 1 < len(tagged) and tagged[j + 1][1] == 'NC':
                # Si hay dos sustantivos juntos, unirlos
                palabras_seleccionadas.append(token + ' ' + tagged[j + 1][0])
                j += 1
            else:
                palabras_seleccionadas.append(token)
        j += 1

    # Separar palabras unidas por "y" o "con"
    palabras_separadas = []
    for palabra in palabras_seleccionadas:
        if ' y ' in palabra:
            palabras_separadas.extend(palabra.split(' y '))
        elif ' con ' in palabra:
            palabras_separadas.extend(palabra.split(' con '))
        elif palabra not in exclusiones:
            palabras_separadas.append(palabra)
    return palabras_separadas


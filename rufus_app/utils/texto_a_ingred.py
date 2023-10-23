import spacy
# cargar el modelo en español
nlp = spacy.load("es_core_news_sm")
# lista de etiquetas POS que queremos mantener
etiquetas = ['NOUN', 'ADJ', 'PROPN']
# lista de palabras que no queremos incluir
exclusiones = ['$', '€', '£', '¥']
# función para procesar cada oración
def procesar_oracion(oracion):
    print('procesa oracion', oracion)
    palabras_seleccionadas = []
    doc_oracion = nlp(oracion)
    j = 0
    while j < len(doc_oracion):
        token = doc_oracion[j]
        if token.pos_ in etiquetas and not token.is_stop:
            if j+1 < len(doc_oracion) and doc_oracion[j+1].text == 'de' and j+2 < len(doc_oracion) and doc_oracion[j+2].pos_ == 'NOUN':
                # Si hay un 'de' entre dos nouns, unirlos en un solo string
                palabra = token.text + ' de ' + doc_oracion[j+2].text
                if j+3 < len(doc_oracion) and doc_oracion[j+3].pos_ == 'NOUN':
                    palabra += ' ' + doc_oracion[j+3].text
                    j += 1
                palabras_seleccionadas.append(palabra)
                j += 2
            elif j+1 < len(doc_oracion) and token.pos_ == 'NOUN' and doc_oracion[j+1].pos_ == 'NOUN':
                # Si hay dos sustantivos juntos, unirlos en un solo string
                palabras_seleccionadas.append(token.text + ' ' + doc_oracion[j+1].text)
                j += 1
            else:
                palabras_seleccionadas.append(token.text)
        j += 1
    # separar palabras unidas por "y" o "con"
    palabras_separadas = []
    for palabra in palabras_seleccionadas:
        if ' y ' in palabra:
            palabras_separadas.extend(palabra.split(' y '))
        elif ' con ' in palabra:
            palabras_separadas.extend(palabra.split(' con '))
        elif palabra not in exclusiones:
            palabras_separadas.append(palabra)
    return palabras_separadas

# cadena de texto con varias oraciones$
if __name__ == '__main__':
    oraciones = ['milanesa de cerdo con papas fritas', 'canelones de cerdo con papas', 'hamburguesa con papas', 'alfajor de dulce de leche']
    palabras_oraciones = []
    for oracion in oraciones:
        # eliminar los precios de la oración
        oracion = oracion.split('$')[0].strip()
        # procesar la oración y añadir la lista de palabras a la lista final
        palabras_oraciones.append(procesar_oracion(oracion))

    print(palabras_oraciones)

from spellchecker import SpellChecker

def corregir_palabra(palabra):
    spell = SpellChecker()
    palabra_corregida = spell.correction(palabra)
    return palabra_corregida

# Ejemplo de uso
palabra = "pizcta"
palabra_corregida = corregir_palabra(palabra)
print(palabra_corregida)

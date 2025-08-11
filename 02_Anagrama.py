"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""

def anagrama(palabra1, palabra2):
    return sorted(palabra1.lower().replace(" ", "")) == sorted(palabra2.lower().replace(" ", ""))

palabra1 = input("Ingrese palabra 1: ")
palabra2 = input("Ingrese palabra 2: ")

if anagrama(palabra1, palabra2):
    print(True)
else:
    print(False)

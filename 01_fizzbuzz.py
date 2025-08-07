""" * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */"""

contador = 1
multiplo_3 = "Fizz"
multiplo_5 = "Buzz"
multiplo_3_5 = "FizzBuzz"

while contador <= 100:
    if contador % 3 == 0 and contador % 5 == 0:
        print(multiplo_3_5)
    elif contador % 3 == 0:
        print(multiplo_3)
    elif contador % 5 == 0:
        print(multiplo_5)
    else:
        print(contador)
    contador += 1
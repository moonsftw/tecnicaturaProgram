"""Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total."""

cadena = input("Ingrese una oración: ")
vocales = ["a", "e", "i", "o", "u"]
longitud = len(cadena)
nroVocales = 0

for letra in cadena:
    if(letra in vocales):
        nroVocales += 1

print(f'La oración tiene {longitud} caracters y {nroVocales} vocales')
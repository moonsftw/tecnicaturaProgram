"""
Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
14. Plantee el algoritmo planteando métodos para su resolución.
"""

numero = input("Ingrese un número del 100 al 999: ")

def sumaDigitos(num): 
    suma = 0
    for i in range(0, len(num)):
        suma += int(num) % 10
        num = int(num) / 10
    return suma

print(sumaDigitos(numero))

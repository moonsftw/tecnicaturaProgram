"""
- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se
encuentra dentro de la primera
"""

cadena1 = input("Ingrese una oración\n")
cadena2 = input("Igrese una palabra para ver si se encuentra en la oración\n")

if cadena2.lower() in cadena1.lower(): 
    print(f'{cadena2} se encuentra en {cadena1}')
else:
    print(f'{cadena2} no se encuentra en {cadena1}')
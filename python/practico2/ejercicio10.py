"""
Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario
pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el
resultado por pantalla.
"""

cadena = input("Ingrese una oración: ")
decision = input("Quiere la oración en mayúscula(M) o en minúscula(m): ")
if(decision == 'M'):
    print(cadena.upper())
elif (decision == "m"):
    print(cadena.lower()) 
else:
    print("Letra no válida")

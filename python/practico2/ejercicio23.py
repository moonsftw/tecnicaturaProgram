"""
Crea un programa donde se pida el ingreso de una cadena y por medio de
recursión mostrar la cadena de forma inversa
"""


def invertirCadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return invertirCadena(cadena[1:]) + cadena[0]
    

cadenaIngresada = input("Ingrese una cadena de texto: \n")
print(invertirCadena(cadenaIngresada))
""" Crea un programa que lea una cadena de texto carácter por carácter usando
recursión """


def imprimirCaracter(cadena):
    if len(cadena) == 0:
        return cadena
    print(cadena[0])
    imprimirCaracter(cadena[1:])

imprimirCaracter('hola')
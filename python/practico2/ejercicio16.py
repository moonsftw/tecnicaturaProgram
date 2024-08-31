"""
Codifique un método que reciba como parámetro una cadena y determine si la
misma contiene o no números
"""

def contieneNros(cadena):
    numeros = 0
    for letra in cadena:
        try:
            int(letra)
            numeros += 1
        except ValueError:
            pass
    if numeros > 0:
        print(f"{cadena} contiene {numeros} números.")
    else:
        print(f"{cadena} no tiene numeros")

mi_cadena = "hola como estas"
contieneNros(mi_cadena)
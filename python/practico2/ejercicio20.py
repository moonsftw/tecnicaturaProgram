class Fraccion: 
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador


class OperacionesFraccion: 
    def main():
        numerdor1 = int(input("Ingrese el valor del numerador de la primera fracción: \n"))
        denominador1 = int(input("Ingrese el valor del denominador de la primera fracción: \n"))
        numerador2 = int(input("Ingrese el valor del numerador de la segunda fracción: \n"))
        denominador2 = int(input("Ingrese el valor del denominador de la segunda fracción: \n"))
        f1 = Fraccion(numerdor1, denominador1)
        f2 = Fraccion(numerador2, denominador2)
        


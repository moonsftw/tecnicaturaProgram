from fractions import Fraction


class Fraccion: 
    def __init__(self, numerador, denominador):

        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")
    
        self.numerador = numerador
        self.denominador = denominador
    
    def sumarFracciones(self, f1, f2):
        return Fraction(f1.numerador, f1.denominador) + Fraction(f2.numerador, f2.denominador)
    
    def restarFracciones(self, f1, f2):
        return Fraction(f1.numerador, f1.denominador) - Fraction(f2.numerador, f2.denominador)
    
    def multiplicarFracciones(self, f1, f2):
        return Fraction(f1.numerador, f1.denominador) * Fraction(f2.numerador , f2.denominador)
    
    def dividirFracciones(self, f1, f2):
        if f2.numerador == 0:
            raise ValueError("El numerador de la segunda fracción no puede ser 0")
        return Fraction(f1.numerador, f1.denominador) / Fraction(f2.numerador, f2.denominador)
    
        
   


class OperacionesFraccion: 

    @staticmethod
    def main():
        try:
            numerador1 = int(input("Ingrese el valor del numerador de la primera fracción: \n"))
            denominador1 = int(input("Ingrese el valor del denominador de la primera fracción: \n"))
            numerador2 = int(input("Ingrese el valor del numerador de la segunda fracción: \n"))
            denominador2 = int(input("Ingrese el valor del denominador de la segunda fracción: \n"))
            f1 = Fraccion(numerador1, denominador1)
            f2 = Fraccion(numerador2, denominador2)

            operacion = Fraccion(0,1)

            print(f'Suma: {operacion.sumarFracciones(f1, f2)}') 
            print(f'Resta: {operacion.restarFracciones(f1,f2)}') 
            print(f'Multiplicar: {operacion.multiplicarFracciones(f1,f2)}') 
            print(f'División: {operacion.dividirFracciones(f1,f2)}') 
        except ValueError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    OperacionesFraccion.main()
class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.nombre_operacion = None

    
    def sumarNumeros(self):
        return self.valor1 + self.valor2
    
    def restarNumeros(self):
        return self.valor1 - self.valor2
    
    def multiplicarNumeros(self):
        return self.valor1 * self.valor2
    def dividirNumeros(self):
        if(self.valor2 == 0):
            return "No se puede divir por 0"
        else:
            return self.valor1 / self.valor2
        
    def aplicarOperacion(self, nombre_operacion):
        self.nombre_operacion = nombre_operacion
        if self.nombre_operacion == '+':
            return self.sumarNumeros()
        elif self.nombre_operacion == '-':
            return self.restarNumeros()
        elif self.nombre_operacion == '*':
            return self.multiplicarNumeros()
        elif self.nombre_operacion == '/':
            return self.dividirNumeros()
        else:
            return "Operacion no registrada"
            
class Calculo: 
    def main(self):
        operacion = OperacionMatematica(2,3)

        print(f'Suma: {operacion.aplicarOperacion('+')}')
        print(f'Resta: {operacion.aplicarOperacion('-')}')
        print(f'Multiplicación: {operacion.aplicarOperacion('*')}')
        print(f'División: {operacion.aplicarOperacion('/')}')

if __name__ == "__main__":
    calculo = Calculo()
    calculo.main()
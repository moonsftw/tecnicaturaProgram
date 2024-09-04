"Suma los dígitos de un número ingresado por el usuario de forma recursiva. "

def sumaDigitos(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sumaDigitos(num // 10)
    

numero = int(input("Ingrese un número: "))


print(sumaDigitos(numero))
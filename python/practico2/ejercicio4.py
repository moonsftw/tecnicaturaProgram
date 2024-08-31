"""
Desarrolle un programa que ayude a una cajera a determinar el número de billetes y
monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50,
20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de
dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete
de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05
centavos. Plantee el algoritmo planteando métodos para su resolución.
"""

monto = float(input("Ingrese el monto de dinero: $"))
billetes = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]
tipo = ["billetes"] * 8 + ["monedas"] * 4
for i in range(len(billetes)):
    cantidad = monto // billetes[i]
    monto = round(monto - cantidad * billetes[i], 2)
    if( cantidad > 0):
        print(f'Necesita {cantidad} {tipo[i]} de ${billetes[i]}')





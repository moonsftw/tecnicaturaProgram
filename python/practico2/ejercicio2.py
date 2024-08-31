"""
Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique
"""
# Python devuelve un error tipo ValueError: invalid literal for int() with base 10: 'hola'
# Por ejemplo: 
a = "hola"
print(int(a))

Indique si en Python existen o no variables de tipo valor y su contraparte tipo
referencia como sucede en otros lenguajes como Java.


RESPUESTA:
En python los conceptos de llamar por valor (call by value) o llamar por referencia (call by reference) no son 
usados explicitamente, ya que en realidad depende del tipo de dato que pasamos como argumento en la función, es decir, 
si es mutable (puede cambiar) o inmutable (no puede ser modificado)
- Call by value: cuando pasamos un objeto inmutable( como string, o integers) a una función, se crea una copia de este objeto,
por lo que estamos modificando una copia del objeto dentro de la función, 
```python
def llamar_por_valor(x):
    x = x * 2
    print("Dentro de la función, el valor de x: ", x)
    return

num = 6
print("Número antes de llamar a la función: ", num)
llamar_por_valor(num)
print("Número despues de llamar a la función: ", num)
```
### Output
```
 Número antes de llamar a la función: 6
 Dentro de la función, el valor de x: 12
 Número despues de llamar a la función: 6
```

- Call by reference: cuando pasamos a una función un objeto mutable (como listas o diccionarios), la referencia al espacio de memoria es pasado
a la función. Por lo que al modificarlo dentro de la función se modifica ese espacio de memoria

```python
def llamar_por_referencia(lista):
    lista.append("D")
    print("Dentro de la función, la lista: ", lista)
    return

mi_lista = ["E"]
print("Lista antes de llamar a la función: ", mi_lista)
llamar_por_referencia(mi_lista)
print("Lista despues de llamar a la función: ", mi_lista)
```
### Output
```
 Lista antes de llamar a la función: ["E"]
 Dentro de la función, la lista: ["E", "D"]
 Lista despues de llamar a la función: ["E", "D"]
```
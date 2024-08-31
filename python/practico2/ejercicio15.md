Indique que sucede si realizo la siguiente declaración de variable:
```python
x = None 
print(x) 
```

La palabra reservada None se utiliza para definir un valor nulo, o un no valor
Esto no quiere decir que None sea lo mismo que 0, False, o un string vacío. 

> **None es un tipo de dato(NoneType) y solo None puede ser None**

### Ejemplo

```python
x = None

if x: 
    print("¿Crees que None es lo mismo que True?")
elif x is False:
    print("¿Crees que None es lo mismo que False?")
else: 
    print("None no es ni True, ni False, None es simplemente None...")    
```


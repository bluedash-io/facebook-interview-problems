# Triple suma (3sum)
Implementa una función que reciba un array de enteros y devuelva todos los tríos que sumen 0.

🧩 Algoritmo de 3sum

Dado un array de enteros nums, devuelve todos los tríos `[nums[i],nums[j],nums[k]]` tales que:

-  i ≠ j, i ≠ k y j ≠ k.
- nums[i] + nums[j] + nums[k] = 0.

Ten en cuenta que el conjunto de soluciones no debe contener tríos duplicados.

### Ejemplo 1:
Entrada:
```python
nums = [-1,0,1,2,-1,-4]
```

Salida:
```python
[[-1,-1,2],[-1,0,1]]
```

Explicación:
```python
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
```
Los tríos distintos son [-1,0,1] y [-1,-1,2].

El orden de la salida y el orden de los tríos no importan.

### Ejemplo 2:
Entrada:
```python
nums = [0,1,1]
```

Salida:
```python
[]
```

Explicación:

El único trío posible no suma 0.

### Ejemplo 3:

Entrada:
```python
nums = [0,0,0]
```

Salida:
```python
[[0,0,0]]
```

Explicación:

El único trío posible suma 0.
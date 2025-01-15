# Convertir String a Entero (myAtoi)
Implementa la función myAtoi(string s), que convierte un string en un entero con signo de 32 bits.

# 🧩 Algoritmo de myAtoi
El proceso para convertir el string a un entero sigue los siguientes pasos:

1. Espacios en blanco:
Ignora cualquier espacio en blanco inicial (" ").

2. Signo:
Determina el signo verificando si el siguiente carácter es '-' o '+'.

    - Si no hay ningún signo, se asume que es positivo.

3. Conversión:
Lee los caracteres numéricos (dígitos) hasta que encuentres un carácter que no sea un dígito o llegues al final del string.

    - Ignora ceros iniciales.
    - Si no se encuentran dígitos, el resultado es 0.

Rango:
Asegúrate de que el número esté dentro del rango permitido para enteros con signo de 32 bits:

<code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>
Si el número es menor que -2^{31}, redondea a -2^{31}.
Si el número es mayor que 2^{31} - 1, redondea a 2^{31} - 1.

Resultado:
Devuelve el entero final.

### Ejemplo 1:
Entrada:

```python
s = "42"
```
Salida:

```python
42
```
Explicación:

1. No hay espacios en blanco iniciales: "42".
2. No hay signo explícito: se asume positivo.
3. Se leen los dígitos: "42".
4. El número está dentro del rango permitido.
5. Resultado final: 42.

### Ejemplo 2:
Entrada:

```python
s = "   -042"
```
Salida:

```python
-42
```
Explicación:
1. Se ignoran los espacios en blanco: " -042".
2. Se detecta el signo negativo: '-'.
3. Se leen los dígitos: "042", ignorando los ceros iniciales.
4. El número está dentro del rango permitido.
5. Resultado final: -42.

### Ejemplo 3:
Entrada:

```python
s = "1337c0d3"
```
Salida:

```python
1337
```
Explicación:
1. No hay espacios en blanco iniciales: "1337c0d3".
2. No hay signo explícito: se asume positivo.
3. Se leen los dígitos: "1337". La lectura se detiene en el primer carácter no numérico ('c').
4. El número está dentro del rango permitido.
5. Resultado final: 1337.

### Ejemplo 4:
Entrada:

```python
s = "0-1"
```
Salida:

```python
0
```
Explicación:
1. No hay espacios en blanco iniciales: "0-1".
2. No hay signo explícito: se asume positivo.
3. Se lee el dígito "0". La lectura se detiene en el guion ('-') porque no es un dígito.
4. Resultado final: 0.

### Ejemplo 5:
Entrada:

```python
s = "words and 987"
```
Salida:

```python
0
```
Explicación:
1. La lectura se detiene en el primer carácter no numérico ('w')
2. No hay dígitos que convertir.
3. Resultado final: 0.

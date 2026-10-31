# PAPR Práctica 1
Lucía Sánchez Manso

## 1. Palíndromos

Imperativa: Crearía una lista vacía, se abriría un bucle `for` para recorrer palabra por palabra, se comprobaría si se lee igual al derecho que al revés y se haría un `.append()`con `True` o `False`.

Funcional: Bucles explícitos y mutación de variables se sustituyen con funciones puras y funciones de orden superior.

  1. Función pura (`es_palindromo`): Recibe dato, calcula resultado sin modificar nada fuera de ella y lo devuelve
  2. Operador funcional `map`: Toma una función y un iterable y aplica esa función a cada elemento de forma automática.

## 2. Suma Cuadrados
Imperativa: Crearía una variable `suma = 0` (estado mutable) abriría un bucle `for i in range(1, n +1)` en cada vuelta modificaría `suma += i ** 2`.

Funcional: No existen cambios de estado ni variables acumuladoras. Se realiza todo mediante llamadas a funciones anidadas.

  1. Generación: Crear colección de números del 1 al n
  2. Transformación (`map`): Cada número a un cuadrado
  3. Reducción: Combinar todos los elementos cuadrados por pares mediante una suma hasta tener un valor final.

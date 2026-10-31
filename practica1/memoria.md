# PAPR Práctica 1
Lucía Sánchez Manso

## 1. Palíndromos

Imperativa: Para comprobar una lista de palabras se crearía una lista vacía, se abriría un bucle `for` para recorrer palabra por palabra, se comprobaría si se lee igual al derecho que al revés y se haría un `.append()`con `True` o `False`.

Funcional: Bucles explícitos y mutación de variables se sustituyen con funciones puras y funciones de orden superior.

  1. Función pura (`es_palindromo`): Recibe dato, calcula resultado sin modificar nada fuera de ella y lo devuelve
  2. Operador funcional `map`: Toma una función y un iterable y aplica esa función a cada elemento de forma automática.

## 2. Suma Cuadrados
Imperativa: 
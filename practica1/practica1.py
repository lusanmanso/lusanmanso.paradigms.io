from functools import reduce

# EJ 1

# Slicing recorriendo la cadena hacia atrás
def es_palindromo(s):
  return s == s[::-1]

def palindromos(lista_strings):
  return list(map(es_palindromo, lista_strings)) # Se entrega la función a sí misma para que map la use

print("\n--- Pruebas de palindromos ---")
print("1. Mixta:", palindromos(["radar", "gato", "oso", "perro"]))
print("2. Todos True:", palindromos(["ana", "otto", "seres", " kayak".strip()]))
print("3. Todos False:", palindromos(["cat", "dog", "hedgehog", "gecko"]))
print("4. Un carácter y vacía:", palindromos(["a", "", "b", "ab"]))
print("5. Números en string:", palindromos(["12321", "12345", "11", "10"]))

# EJ 2

# Dividí en funciones puras por separado porque una línea de lambda no la entiendo
# Ambas devuelven un único valor directamente de su param de entrada y no hay estado mutable
def elevar_al_cuadrado(x):
  return x ** 2

def sumar_dos_numeros(acc, nuevo_num):
  return acc + nuevo_num

# Se pasan como args dentro de los objetos
def cuadrados_sumados(n):
  nums = range(1, n +1)

  cuadrados = map(elevar_al_cuadrado, nums)

  sum_total = reduce(sumar_dos_numeros, cuadrados, 0)
  return sum_total

print("--- Pruebas de cuadrados_sumados ---")
print("1. n = 1:", cuadrados_sumados(1))   # 1
print("2. n = 3:", cuadrados_sumados(3))   # 14
print("3. n = 4:", cuadrados_sumados(4))   # 30
print("4. n = 5:", cuadrados_sumados(5))   # 55
print("5. n = 10:", cuadrados_sumados(10)) # 385

from functools import reduce
import requests
import hashlib

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

def sumar_nuevo_num (acc, nuevo_num):
  return acc + nuevo_num

# Se pasan como args dentro de los objetos
def cuadrados_sumados(n):
  nums = range(1, n +1)

  cuadrados = map(elevar_al_cuadrado, nums)

  sum_total = reduce(sumar_nuevo_num, cuadrados, 0)
  return sum_total

print("--- Pruebas de cuadrados_sumados ---")
print("1. n = 1:", cuadrados_sumados(1))   # 1
print("2. n = 3:", cuadrados_sumados(3))   # 14
print("3. n = 4:", cuadrados_sumados(4))   # 30
print("4. n = 5:", cuadrados_sumados(5))   # 55
print("5. n = 10:", cuadrados_sumados(10)) # 385

# EJ 3


def multiplicar(acc, nuevo_num):
  return acc * nuevo_num


def factorial(n):
  nums = range(1, n + 1)
  res = reduce(multiplicar, nums, 1)

  return res

print("--- Pruebas de factorial ---")
print("1. Factorial de 0:", factorial(0))  # Caso base: 0! = 1
print("2. Factorial de 1:", factorial(1))  # 1
print("3. Factorial de 4:", factorial(4))  # 24
print("4. Factorial de 5:", factorial(5))  # 120
print("5. Factorial de 6:", factorial(6))  # 720

# EJ 4

estudiantes = [
    {"nombre": "Juan", "calificaciones": [7, 8, 6]},
    {"nombre": "Ana", "calificaciones": [5, 4, 5]},
    {"nombre": "Pedro", "calificaciones": [6, 6, 6]},
    {"nombre": "Maria", "calificaciones": [9, 10, 8]},
    {"nombre": "Luis", "calificaciones": [3, 5, 4]}
]

def sumar(a, b):
  return a + b

def promedio(notas):
  suma_notas = reduce(sumar, notas, 0)
  cantidad_notas = len(notas)
  return suma_notas / cantidad_notas
# return reduce(lambda a, b: a + b, notas, 0) / len(notas)

def filtrar_estudiantes(lista_estudiantes):
  aprobados = filter(lambda estudiantes: promedio(estudiantes["calificaciones"]) >= 6, estudiantes)
  return list(aprobados)

print("--- Pruebas de filtrado de estudiantes (promedio >= 6) ---")
# Juan, Pedro y Maria aprueban; Ana y Luis suspenden)
print(filtrar_estudiantes(estudiantes))

# EJ 5 - HaveIBeenPawned

# Generación de hashes en formato estándar y Windows NTLM
def generar_hash_sha1(pass):
  txt_bytes = pass.encode('utf-8')
  hash_hex = hashlib.sha1(txt_bytes).hexdigest()
  return hash_hex.upper()

def generar_hash_ntlm(pass):
  txt_bytes = pass.encode('utf-16le')
  hash_hex = hashlib.new('md4', txt_bytes).hexdigest()
  return hash_hex.upper()


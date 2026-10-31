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

def suma_cuadrados(n):

from functools import reduce
import request
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
def gen_hash_sha1(pwd):
  txt_bytes = pwd.encode('utf-8')
  hash_hex = hashlib.sha1(txt_bytes).hexdigest()
  return hash_hex.upper()

def gen_hash_ntlm(pwd):
  txt_bytes = pwd.encode('utf-16le')
  hash_hex = hashlib.new('md4', txt_bytes).hexdigest()
  return hash_hex.upper()

# Callback general para errores
def errors(err_msg):
  print(f"[[ERROR]]: {err_msg}")


# Gestión de peticiones
def request(url, callback_success, callback_error):
  try:
    answer = requests.get(url, timeout = 10)
    if answer.status_code == 200:
      callback_success(respuesta)
    else:
      callback_error(f"HTTP status code {respuesta.status_code} in {url}")
  except requests.exceptions.RequestException as e:
    callback_error(f"Connection error: {e}")

# Callback éxito para dominios
def show_domain_breach(answer):
  breaches = answer.json()
  if not breaches:
    print("No breaches for this domain.")
  else:
    format_breach =  lambda b: f" - {b.get('Title', 'No Title')} (Date: {b.get('BreachDate', 'N/A')}, Affected Accounts: {b.get('PwnCount', 0)})"
    txt_list = list(map(format_breach, breaches))
    prin(f"Found {len(txt_list)} breaches for this domain: \n" + "\n".join(txt_list))

# Comprueba contraseña con CALLBACK tipo hash
def check_password(pwd, callback_hash, ntml_mode=False):
  full_hash = callback_hash(pwd) # Invocar el callback para obtener tipo

  prefix = full_hash[:5] # Primeros 5 caracteres son el sufijo
  sufix = full_hash[5:] # El resto

  # Construir la URL según el formato
  if ntml_mode:
    url = f"https://api.pwnedpasswords.com/range/{prefix}?mode=ntlm"
  else:
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

  def verify_sufix(answer):
    lines = answer.text.splitlines()
    matches = list(filter(lambda line : line.startswith(sufix), lines))

    if matches:
      times = matches[0].split(":")[1]
      print(f"Password {pwd} appeared {times} times in data breaches.")
    else:
      print(f"Password {pwd} does not appear in any data breaches.")

  request(url, verify_sufix, errors)

# Comprobación
def check_domain(domain):
  url = f"https://haveibeenpwned.com/api/v3/breaches?Domain={domain}"
  request(url, show_domain_breach, error)

# Menú de elección
def menu():
    print("\n=== HAVE I BEEN PWNED ===")
    print("1. Searching by range (contraseñas)")
    print("2. Breached sites (dominios)")
    modo = input("Selecciona (1 o 2): ").strip()

    if modo == "1":
        format = input("Especifica formato HASH - Estándar (SHA1) o Windows (NTLM): ").strip().upper()
        pwd = input("Introducir contraseña a verificar: ")

        if format == "SHA1":
            # Pasamos la función generar_hash_sha1 como CALLBACK (sin paréntesis)
            check_password(pwd, generar_hash_sha1, modo_ntlm=False)
        elif formato == "NTLM":
            # Pasamos la función generar_hash_ntlm como CALLBACK (sin paréntesis)
            check_password(pwd, generar_hash_ntlm, modo_ntlm=True)
        else:
            error("Formato de hash no válido. Debe elegir SHA1 o NTLM.")

    elif modo == "2":
        dominio = input("Introduzca el dominio a consultar (ej. adobe.com): ").strip()
        check_domain(dominio)
    else:
        error("Modo no reconocido. Seleccionar 1 o 2.")

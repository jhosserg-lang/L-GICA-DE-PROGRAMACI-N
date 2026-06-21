import random
import string

print("=================================")
print(" GENERADOR SEGURO DE CONTRASEÑAS ")
print("=================================")

# Solicitar longitud
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Opciones
usar_mayusculas = input(
    "¿Incluir mayúsculas? (s/n): "
).lower()

usar_numeros = input(
    "¿Incluir números? (s/n): "
).lower()

usar_especiales = input(
    "¿Incluir caracteres especiales? (s/n): "
).lower()

# Conjunto base
caracteres = string.ascii_lowercase

# Condicionales
if usar_mayusculas == "s":
    caracteres += string.ascii_uppercase

if usar_numeros == "s":
    caracteres += string.digits

if usar_especiales == "s":
    caracteres += string.punctuation

# Generación usando bucle
contrasena = ""

for i in range(longitud):
    contrasena += random.choice(caracteres)

print("\nContraseña generada:")
print(contrasena)
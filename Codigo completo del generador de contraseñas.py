import random
import string

# Lista para guardar el historial
historial = []

# Función para evaluar la fortaleza
def evaluar_fortaleza(longitud, mayus, nums, esp):

    puntos = 0

    if longitud >= 8:
        puntos += 1

    if longitud >= 12:
        puntos += 1

    if mayus:
        puntos += 1

    if nums:
        puntos += 1

    if esp:
        puntos += 1

    if puntos <= 2:
        return "🔴 Débil"

    elif puntos <= 4:
        return "🟡 Media"

    else:
        return "🟢 Fuerte"


# Función para generar contraseña
def generar():

    while True:

        try:

            longitud = int(input("\nIngrese la longitud (mínimo 4): "))

            if longitud >= 4:
                break

            print("La longitud debe ser mínimo 4.")

        except ValueError:

            print("Ingrese un número válido.")

    mayus = input("¿Incluir mayúsculas? (S/N): ").upper() == "S"
    numeros = input("¿Incluir números? (S/N): ").upper() == "S"
    especiales = input("¿Incluir caracteres especiales? (S/N): ").upper() == "S"

    caracteres = string.ascii_lowercase

    if mayus:
        caracteres += string.ascii_uppercase

    if numeros:
        caracteres += string.digits

    if especiales:
        caracteres += string.punctuation

    contraseña = ""

    for i in range(longitud):
        contraseña += random.choice(caracteres)

    fortaleza = evaluar_fortaleza(
        longitud,
        mayus,
        numeros,
        especiales
    )

    historial.append(contraseña)

    print("==============================")
    print("Contraseña generada:")
    print(contraseña)
    print("Fortaleza:", fortaleza)
    print("==============================")


# Mostrar historial
def mostrar_historial():

    if len(historial) == 0:

        print("\nNo existen contraseñas generadas.")

    else:

        print("\n===== HISTORIAL =====")

        for i, c in enumerate(historial, start=1):

            print(f"{i}. {c}")


# Programa principal

while True:

    print("==============================")
    print(" GENERADOR DE CONTRASEÑAS")
    print("==============================")
    print("1. Generar contraseña")
    print("2. Ver historial")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        generar()

    elif opcion == "2":

        mostrar_historial()

    elif opcion == "3":

        print("Gracias por utilizar el programa.")
        break

    else:

        print("Opción no válida.")
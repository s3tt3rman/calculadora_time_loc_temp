import os
nombre = os.getlogin()


import re
import datetime
from termcolor import colored


# Saludo y hora actual
ahora = datetime.datetime.now()
print(f"Hola, {nombre}!\nLa hora actual es: {ahora:%H:%M:%S}\n")


# Iniciar operaciones matemáticas
opcion = input("¿Desea iniciar operaciones matemáticas? (S/N) ").lower()
while opcion == "s":
    # Obtener la hora actual
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

    # Pedir la operación al usuario
    operacion_completa = input(f"[{hora_actual}] Ingrese la operación que desea realizar (ejemplo: 3+5): ")

    # Validar la operación ingresada
    while not re.match(r'^\d+[\+\-\*/]\d+$', operacion_completa):
        operacion_completa = input("Operación inválida. Ingrese una operación válida (ejemplo: 3+5): ")

    # Realizar la operación
    operando1, operador, operando2 = re.findall(r'\d+|\D+', operacion_completa)
    resultado = eval(f"{operando1}{operador}{operando2}")

    # Imprimir el resultado
    print(colored(f"El resultado es: {resultado}", "red", attrs=["bold"]))

    # Preguntar al usuario si desea realizar otra operación
    opcion = input("¿Desea realizar otra operación? (S/N) ").lower()

# Despedirse del usuario
print("Adiós!")

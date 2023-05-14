"""
MATH v1.5.75

Author: S3tt3R
Date: may 2023
"""

from ubicacion import obtener_localizacion
from temperatura import obtener_temperatura
import os
import re
import datetime
from termcolor import colored

# Saludo y hora actual
ahora = datetime.datetime.now()
nombre = os.getlogin()
print(f"Hola, {nombre}!\nLa hora actual es: {ahora:%H:%M:%S}\n")

# Localizacion
localizacion = obtener_localizacion()
if localizacion:
    print(f"Estás ubicado en: {localizacion}\n")

# Temp localizacion
temperatura_actual = obtener_temperatura()
print(f"Temperatura actual: {temperatura_actual}\n") 

# Funciones para operaciones matemáticas
def evaluar_operacion(operacion):
    try:
        resultado = round(eval(operacion), 2)
        return resultado
    except:
        return None

def realizar_operacion():
    operacion_completa = input("Ingrese la operación que desea realizar (ejemplo: 3x5): ")
    while not re.match(r'^\d+(\.\d{1,2})?[+\-*/]\d+(\.\d{1,2})?$', operacion_completa):
        operacion_completa = input("Operación inválida. Ingrese una operación válida (ejemplo: 3x5): ")
    operacion = re.sub(r'([+\-*/])', r' \1 ', operacion_completa)
    resultado = evaluar_operacion(operacion)
    if resultado is None:
        print(colored("Operación inválida.", "red", attrs=["bold"]))
    else:
        print(colored(f"El resultado es: {resultado}", "red", attrs=["bold"]))

# Iniciar operaciones matemáticas
opcion = input("¿Desea iniciar operaciones matemáticas? (S/N) ").lower()
while opcion == "s":
    realizar_operacion()
    opcion = input("¿Desea realizar otra operación? (S/N) ").lower()

# Despedirse del usuario
print("Adiós!")

"""
TEMPERATURA DE LA UBICACION

Author: S3tt3R
Date: may 2023
"""

import requests

def obtener_temperatura():
    try:
        response = requests.get('https://ipapi.co/json/')
        if response.status_code == 200:
            data = response.json()
            ciudad = data['city']
            pais = data['country']
            api_key = "S3tt3R.weather"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperatura = data["main"]["temp"]
                return f"La temperatura actual en {ciudad} es de {temperatura} grados Celsius."
            else:
                return "No se pudo obtener la temperatura actual."
        else:
            return "No se pudo obtener la ubicación actual."
    except:
        return "No se pudo obtener la temperatura actual."
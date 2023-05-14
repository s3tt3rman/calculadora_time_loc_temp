"""
LOCALIZACION

Author: S3tt3R
Date: may 2023
"""
import requests

def obtener_localizacion():
    try:
        response = requests.get("https://ipinfo.io/")
        data = response.json()
        ciudad = data["city"]
        pais = data["country"]
        return f"{ciudad}, {pais}"
    except:
        return None
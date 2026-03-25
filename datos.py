import json

ARCHIVO = "datos.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(aeronaves):
    with open(ARCHIVO, "w") as f:
        json.dump(aeronaves, f, indent=4)
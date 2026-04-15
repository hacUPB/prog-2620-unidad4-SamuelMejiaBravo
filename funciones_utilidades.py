# funciones_utilidades.py
# Funciones auxiliares para cargar y guardar datos en JSON

import json
import os

ARCHIVO_AERONAVES = "datos_aeronaves.json"
ARCHIVO_COMPONENTES = "datos_componentes.json"


def cargar_datos_json():
    """
    Carga los datos de aeronaves desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if os.path.exists(ARCHIVO_AERONAVES):
        try:
            with open(ARCHIVO_AERONAVES, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos.get("aeronaves", [])
        except:
            return []
    return []


def cargar_componentes_json():
    """
    Carga los datos de componentes desde el archivo JSON.
    Retorna un diccionario con matricula: {componentes}
    """
    if os.path.exists(ARCHIVO_COMPONENTES):
        try:
            with open(ARCHIVO_COMPONENTES, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except:
            return {}
    return {}


def guardar_datos_json(aeronaves):
    """
    Guarda los datos de aeronaves en el archivo JSON.
    """
    datos = {"aeronaves": aeronaves}
    with open(ARCHIVO_AERONAVES, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def guardar_componentes_json(componentes):
    """
    Guarda los datos de componentes en el archivo JSON separado.
    Componentes es un diccionario de {matricula: {nombre_componente: datos}}
    """
    with open(ARCHIVO_COMPONENTES, "w", encoding="utf-8") as archivo:
        json.dump(componentes, archivo, indent=4, ensure_ascii=False)

# funciones_aeronaves.py
# Funciones para gestionar aeronaves

from funciones_utilidades import cargar_datos_json, guardar_datos_json
from funciones_menu import SalidaPrograma


def registrar_aeronaves():
    """
    Permite al usuario registrar aeronaves.
    Retorna una lista de diccionarios con la información de cada aeronave.
    Los datos se guardan automáticamente en el archivo JSON.
    El usuario puede escribir 'v' para volver al menú principal o 'f' para cerrar.
    """
    aeronaves = cargar_datos_json()
    
    print("\n" + "="*60)
    print("REGISTRO DE AERONAVES")
    print("="*60)
    print("(Escriba 'v' para volver o 'f' para cerrar en cualquier campo)\n")
    
    numero_aeronaves = 1
    
    while True:
        print(f"\n--- Aeronave {numero_aeronaves} ---")
        
        matricula = input("Ingrese la matrícula (ej. HK-4532) o v/f: ").strip()
        if matricula.lower() == "f":
            raise SalidaPrograma()
        if matricula.lower() == "v":
            if len(aeronaves) > 0:
                print(f"Se guardaron {len(aeronaves)} aeronave(s).")
            return aeronaves
        
        modelo = input("Ingrese el modelo (ej. A320, ATR72) o v/f: ").strip()
        if modelo.lower() == "f":
            raise SalidaPrograma()
        if modelo.lower() == "v":
            if len(aeronaves) > 0:
                print(f"Se guardaron {len(aeronaves)} aeronave(s).")
            return aeronaves
        
        while True:
            try:
                horas_vuelo_input = input("Ingrese las horas de vuelo acumuladas o v/f: ").strip()
                if horas_vuelo_input.lower() == "f":
                    raise SalidaPrograma()
                if horas_vuelo_input.lower() == "v":
                    if len(aeronaves) > 0:
                        print(f"Se guardaron {len(aeronaves)} aeronave(s).")
                    return aeronaves
                horas_vuelo = float(horas_vuelo_input)
                break
            except ValueError:
                print("Error: Ingrese un número válido")
        
        # Crear diccionario para la aeronave
        aeronave = {
            "matricula": matricula,
            "modelo": modelo,
            "horas_vuelo": horas_vuelo
        }
        
        aeronaves.append(aeronave)
        print("Aeronave registrada correctamente.")
        
        # Preguntar si desea registrar otra aeronave
        while True:
            continuar = input("\nDesea registrar otra aeronave? (s/n/f): ").strip().lower()
            if continuar == "f":
                raise SalidaPrograma()
            if continuar == "s":
                numero_aeronaves += 1
                break
            elif continuar == "n":
                # Guardar datos en JSON
                guardar_datos_json(aeronaves)
                return aeronaves
            else:
                print("Por favor, responda con 's' o 'n'.")

# Programa principal ejecutable - Sistema de Gestión de Aeronaves y Componentes

from funciones_utilidades import cargar_datos_json, cargar_componentes_json
from funciones_aeronaves import registrar_aeronaves
from funciones_componentes import registrar_componentes, editar_componentes
from funciones_calculos import generar_reporte_mantenimiento, mostrar_resumen_sistema
from funciones_menu import mostrar_menu, SalidaPrograma
from cache_del import limpiar_cache
import os
import shutil
from pathlib import Path

limpiar_cache()
"Archivos caché limpiados. Iniciando programa principal."
def main():
    """Función principal del programa."""
    # Cargar datos existentes del JSON
    aeronaves = cargar_datos_json()
    componentes_dict = cargar_componentes_json()
    
    aeronaves_registradas = len(aeronaves) > 0
    componentes_registrados = False    # NO es NULL
    
    # Verificar si hay componentes registrados
    if len(componentes_dict) > 0:
        componentes_registrados = True
    
    print("\n🪽BIENVENIDO AL SISTEMA DE GESTIÓN DE MANTENIMIENTO🪽")
    
    try:
        while True:
            opcion = mostrar_menu()
            
            if opcion == "1":
                # Registrar aeronaves
                aeronaves = registrar_aeronaves()
                aeronaves_registradas = True
                print("\nAeronaves registradas correctamente.")
            
            elif opcion == "2":
                # Registrar componentes
                if not aeronaves_registradas or len(aeronaves) == 0:
                    print("\nError: Primero debe registrar las aeronaves (opción 1).")
                else:
                    volvio = registrar_componentes(aeronaves)
                    if volvio is True:
                        print("\nHa vuelto al menú principal.")
                        # Recargar componentes en caso de cambios
                        componentes_dict = cargar_componentes_json()
                        if len(componentes_dict) > 0:
                            componentes_registrados = True
                    elif volvio is False:
                        componentes_dict = cargar_componentes_json()
                        componentes_registrados = True
                        print("\nComponentes registrados correctamente.")
            
            elif opcion == "3":
                # Editar componentes
                if not aeronaves_registradas or len(aeronaves) == 0:
                    print("\nError: Primero debe registrar aeronaves y componentes.")
                else:
                    editar_componentes(aeronaves)
            
            elif opcion == "4":
                # Ver reporte de mantenimiento
                if not aeronaves_registradas or not componentes_registrados:
                    print("\nError: Debe registrar aeronaves y componentes primero.")
                else:
                    generar_reporte_mantenimiento(aeronaves)
            
            elif opcion == "5":
                # Ver resumen del sistema
                if not aeronaves_registradas:
                    print("\nError: No hay datos registrados aún.")
                else:
                    mostrar_resumen_sistema(aeronaves)
            
            # Pausa para que el usuario lea los resultados
            if opcion in ["1", "2", "3", "4", "5"]:
                input("\nPresione Enter para continuar...")
    
    except SalidaPrograma:
        print("\n" + "="*60)
        print("Gracias por usar el sistema de gestión de mantenimiento.")
        print("="*60 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
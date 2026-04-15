# funciones_menu.py
# Funciones relacionadas con la interfaz de menú y selección del usuario

class SalidaPrograma(Exception):
    """Excepción para solicitar salida del programa."""
    pass


def mostrar_menu():
    """
    Muestra el menú principal interactivo y retorna la opción seleccionada.
    Las opciones disponibles son:
    1 - Registrar nuevas aeronaves
    2 - Registrar componentes de una aeronave
    3 - Editar componentes de una aeronave
    4 - Ver reporte de mantenimiento
    5 - Ver resumen del sistema
    6 - Fin (cerrar programa)
    """
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE MANTENIMIENTO DE AERONAVES")
    print("="*60)
    print("\nMENÚ PRINCIPAL")
    print("1 - Registrar nuevas aeronaves")
    print("2 - Registrar componentes de una aeronave")
    print("3 - Editar componentes de una aeronave")
    print("4 - Ver reporte de mantenimiento")
    print("5 - Ver resumen del sistema")
    print("6 - Fin (cerrar programa)")
    print("-"*60)
    
    while True:
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "6":
            raise SalidaPrograma()
        
        if opcion in ['1', '2', '3', '4', '5']:
            return opcion
        else:
            print("Opción inválida. Por favor, selecciona 1, 2, 3, 4, 5 o 6.")


def mostrar_menu_aeronaves(aeronaves):
    """
    Muestra un menú para seleccionar una aeronave de la lista y retorna el índice seleccionado.
    Cada aeronave se presenta con un ID (1-based) para facilidad de selección.
    """
    if len(aeronaves) == 0:
        print("No hay aeronaves registradas.")
        return -1
    
    print("\n" + "="*60)
    print("SELECCIONAR AERONAVE")
    print("="*60)
    
    # Mostrar lista de aeronaves con ID
    for i in range(len(aeronaves)):
        aeronave = aeronaves[i]
        print(f"{i + 1}. {aeronave['matricula']} ({aeronave['modelo']})")
    
    print(f"v - Volver al menú principal")
    print("f - Fin (cerrar programa)")
    print("-"*60)
    
    while True:
        try:
            seleccion = input("Selecciona el ID de la aeronave (o v/f): ").strip().lower()
            
            if seleccion == "f":
                raise SalidaPrograma()
            
            if seleccion == "v":
                return -1
            
            # Validar que sea un número válido
            id_seleccion = int(seleccion)
            if 1 <= id_seleccion <= len(aeronaves):
                return id_seleccion - 1  # Convertir a índice 0-based
            else:
                print(f"ID inválido. Selecciona un ID entre 1 y {len(aeronaves)}, v o f.")
        except ValueError:
            print(f"Entrada inválida. Selecciona un ID entre 1 y {len(aeronaves)}, v o f.")


def obtener_entrada_usuario(mensaje, permitir_volver=True):
    """
    Obtiene una entrada del usuario con validación opcional de volver/fin.
    
    Parámetros:
    - mensaje: El mensaje a mostrar al usuario
    - permitir_volver: Si True, el usuario puede escribir v para retornar o f para finalizar
    
    Retorna: Tupla (entrada, volver) donde volver es True si el usuario quiso volver
    """
    while True:
        entrada = input(mensaje).strip()
        
        if permitir_volver and entrada.lower() == "f":
            raise SalidaPrograma()
        
        if permitir_volver and entrada.lower() == "v":
            return None, True
        
        if entrada:
            return entrada, False
        else:
            print("Entrada vacía. Por favor, ingresa un valor, v para volver o f para finalizar.")


def obtener_entrada_numerica(mensaje, minimo=None, maximo=None, permitir_volver=True):
    """
    Obtiene una entrada numérica del usuario con validación de rango opcional.
    
    Parámetros:
    - mensaje: El mensaje a mostrar al usuario
    - minimo: Valor mínimo permitido (opcional)
    - maximo: Valor máximo permitido (opcional)
    - permitir_volver: Si True, el usuario puede escribir v para volver o f para finalizar
    
    Retorna: Tupla (numero, volver) donde volver es True si el usuario quiso volver
    """
    while True:
        entrada = input(mensaje).strip().lower()
        
        if permitir_volver and entrada == "f":
            raise SalidaPrograma()
        
        if permitir_volver and entrada == "v":
            return None, True
        
        try:
            numero = int(entrada)
            
            # Validar rango si se especificó
            if minimo is not None and numero < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
                continue
            
            return numero, False
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número, v para volver o f para finalizar.")

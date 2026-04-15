# funciones_componentes.py
# Funciones para gestionar componentes

from funciones_utilidades import cargar_componentes_json, guardar_componentes_json
from funciones_menu import SalidaPrograma, mostrar_menu_aeronaves


def registrar_componentes(aeronaves):
    """
    Permite registrar componentes críticos para aeronaves seleccionadas.
    El usuario puede elegir qué aeronave registrar y registrar componentes solo para esa.
    Los datos se guardan automáticamente en archivo JSON separado.
    El usuario puede escribir 'v' para volver o 'f' para cerrar.
    """
    # Validar que haya aeronaves registradas
    if len(aeronaves) == 0:
        print("\nError: No hay aeronaves registradas. Debe registrar aeronaves primero.")
        return False
    
    # Cargar componentes existentes
    componentes_dict = cargar_componentes_json()
    
    print("\n" + "="*60)
    print("REGISTRO DE COMPONENTES")
    print("="*60)
    print("(Escriba 'v' para volver o 'f' para cerrar)\n")
    
    while True:
        # Mostrar aeronaves disponibles
        print("\nAeronaves disponibles:\n")
        for i in range(len(aeronaves)):
            matricula = aeronaves[i]['matricula']
            modelo = aeronaves[i]['modelo']
            componentes_count = len(componentes_dict.get(matricula, {}))
            print(f"ID {i + 1}. {matricula} ({modelo}) - {componentes_count} componente(s) registrado(s)")
        
        # Seleccionar aeronave
        print("\n")
        seleccion = input("Ingrese el ID de la aeronave para registrar componentes (o v para volver, f para cerrar): ").strip()
        
        if seleccion.lower() == "f":
            raise SalidaPrograma()
        if seleccion.lower() == "v":
            print("Volviendo al menú principal.")
            return False
        
        # Validar selección
        try:
            id_aero = int(seleccion)
            if 1 <= id_aero <= len(aeronaves):
                break
            else:
                print("ID no válido. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue
        
        print("Error: Ingrese un número válido.")
    
    # Registrar componentes para la aeronave seleccionada
    i = id_aero - 1
    matricula = aeronaves[i]['matricula']
    
    # Crear entrada si no existe
    if matricula not in componentes_dict:
        componentes_dict[matricula] = {}
    
    print(f"\n--- Componentes de {matricula} ({aeronaves[i]['modelo']}) ---")
    print("Ingrese al menos 2 componentes. Escriba 'fin' cuando termine.\n")
    
    numero_componente = 1
    componentes_completos = False
    
    while not componentes_completos:
        nombre_componente = input(f"Nombre del componente {numero_componente} (v para volver, f para cerrar, o fin para terminar): ").strip()
        
        if nombre_componente.lower() == "f":
            raise SalidaPrograma()
        # Si el usuario escribe 'v', salir completamente
        if nombre_componente.lower() == "v":
            if len(componentes_dict[matricula]) >= 2:
                guardar_componentes_json(componentes_dict)
                return True  # Señal de que volvió
            else:
                print(f"Esta aeronave tiene {len(componentes_dict[matricula])} componente(s). Se requieren al menos 2.")
                continuar = input("Desea continuar registrando componentes? (s/n/f): ").strip().lower()
                if continuar == "f":
                    raise SalidaPrograma()
                if continuar == "n":
                    if len(componentes_dict[matricula]) > 0:
                        guardar_componentes_json(componentes_dict)
                    return True
            continue
        
        # Si el usuario escribe 'fin' y hay al menos 2 componentes, se termina esta aeronave
        if nombre_componente.lower() == "fin":
            if len(componentes_dict[matricula]) >= 2:
                componentes_completos = True
                break
            else:
                print("Debe registrar al menos 2 componentes por aeronave.")
                continue
        
        # Validar entrada de horas de uso
        horas_uso = None
        while horas_uso is None:
            try:
                horas_uso_input = input(f"Horas de uso actuales de {nombre_componente} (o v/f): ").strip()
                if horas_uso_input.lower() == "f":
                    raise SalidaPrograma()
                if horas_uso_input.lower() == "v":
                    if len(componentes_dict[matricula]) >= 2:
                        guardar_componentes_json(componentes_dict)
                        return True
                    else:
                        print(f"Esta aeronave tiene {len(componentes_dict[matricula])} componente(s). Se requieren al menos 2.")
                        horas_uso = "salir"
                        break
                horas_uso = float(horas_uso_input)
            except ValueError:
                print("Error: Ingrese un número válido")
        
        if horas_uso == "salir":
            continue
        
        # Validar entrada de límite de horas
        limite_horas = None
        while limite_horas is None:
            try:
                limite_horas_input = input(f"Límite de horas permitidas para {nombre_componente} (o v/f): ").strip()
                if limite_horas_input.lower() == "f":
                    raise SalidaPrograma()
                if limite_horas_input.lower() == "v":
                    if len(componentes_dict[matricula]) >= 2:
                        guardar_componentes_json(componentes_dict)
                        return True
                    else:
                        print(f"Esta aeronave tiene {len(componentes_dict[matricula])} componente(s). Se requieren al menos 2.")
                        limite_horas = "salir"
                        break
                limite_horas = float(limite_horas_input)
            except ValueError:
                print("Error: Ingrese un número válido")
        
        if limite_horas == "salir":
            continue
        
        # Crear diccionario para el componente
        componentes_dict[matricula][nombre_componente] = {
            "horas_uso": horas_uso,
            "limite_horas": limite_horas
        }
        
        numero_componente += 1
        print(f"Componente '{nombre_componente}' registrado correctamente.\n")
    
    # Guardar datos en JSON separado
    guardar_componentes_json(componentes_dict)
    print(f"\nComponentes de {matricula} guardados correctamente.")
    return False  # Completó normalmente


def editar_componentes(aeronaves):
    """
    Permite editar las horas de uso de componentes registrados.
    El usuario puede modificar las horas actuales de cualquier componente.
    """
    # Validar que haya aeronaves registradas
    if len(aeronaves) == 0:
        print("\nError: No hay aeronaves registradas.")
        return
    
    # Cargar componentes existentes
    componentes_dict = cargar_componentes_json()
    
    # Verificar si hay componentes registrados
    if not componentes_dict:
        print("\nError: No hay componentes registrados.")
        return
    
    print("\n" + "="*60)
    print("EDITAR HORAS DE COMPONENTES")
    print("="*60)
    
    # Mostrar aeronaves disponibles
    print("\nAeronaves disponibles:\n")
    for i in range(len(aeronaves)):
        matricula = aeronaves[i]['matricula']
        if matricula in componentes_dict and len(componentes_dict[matricula]) > 0:
            print(f"{i + 1}. {matricula} ({aeronaves[i]['modelo']})")
            partes = list(componentes_dict[matricula].keys())
            for j, parte in enumerate(partes):
                datos = componentes_dict[matricula][parte]
                print(f"   - {parte}: {datos['horas_uso']} / {datos['limite_horas']} horas")
    
    # Seleccionar aeronave
    while True:
        try:
            opcion_aero = input("\nSeleccione el número de la aeronave (o v para volver, f para cerrar): ").strip()
            if opcion_aero.lower() == "f":
                raise SalidaPrograma()
            if opcion_aero.lower() == "v":
                return
            
            opcion_aero = int(opcion_aero)
            if 1 <= opcion_aero <= len(aeronaves):
                matricula_seleccionada = aeronaves[opcion_aero - 1]['matricula']
                if matricula_seleccionada in componentes_dict:
                    break
                else:
                    print("Esta aeronave no tiene componentes registrados.")
            else:
                print("Seleccione un número válido.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    
    # Mostrar componentes de la aeronave seleccionada
    print(f"\nComponentes de {matricula_seleccionada}:\n")
    componentes_lista = list(componentes_dict[matricula_seleccionada].items())
    
    for i, (nombre, datos) in enumerate(componentes_lista):
        print(f"{i + 1}. {nombre}")
        print(f"   Horas actuales: {datos['horas_uso']} / {datos['limite_horas']}")
    
    # Seleccionar componente
    while True:
        try:
            opcion_comp = input("\nSeleccione el número del componente a editar (o v para volver, f para cerrar): ").strip()
            if opcion_comp.lower() == "f":
                raise SalidaPrograma()
            if opcion_comp.lower() == "v":
                return
            
            opcion_comp = int(opcion_comp)
            if 1 <= opcion_comp <= len(componentes_lista):
                nombre_componente = componentes_lista[opcion_comp - 1][0]
                break
            else:
                print("Seleccione un número válido.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    
    # Editar horas de uso
    print(f"\nComponente actual: {nombre_componente}")
    print(f"Horas de uso: {componentes_dict[matricula_seleccionada][nombre_componente]['horas_uso']}")
    print(f"Límite permitido: {componentes_dict[matricula_seleccionada][nombre_componente]['limite_horas']}")
    
    while True:
        try:
            nuevas_horas = input("\nIngrese las nuevas horas de uso (o v para volver, f para cerrar): ").strip()
            if nuevas_horas.lower() == "f":
                raise SalidaPrograma()
            if nuevas_horas.lower() == "v":
                print("Operación cancelada.")
                return
            
            nuevas_horas = float(nuevas_horas)
            
            # Actualizar componente
            componentes_dict[matricula_seleccionada][nombre_componente]['horas_uso'] = nuevas_horas
            guardar_componentes_json(componentes_dict)
            
            print(f"\nComponente actualizado correctamente.")
            print(f"Nuevas horas: {nuevas_horas} / {componentes_dict[matricula_seleccionada][nombre_componente]['limite_horas']}")
            break
            
        except ValueError:
            print("Error: Ingrese un número válido.")

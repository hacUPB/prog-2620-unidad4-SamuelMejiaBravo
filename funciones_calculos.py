# funciones_calculos.py
# Funciones de cálculo, análisis y generación de reportes

from funciones_utilidades import cargar_componentes_json


def generar_reporte_mantenimiento(aeronaves):
    """
    Genera un reporte de componentes que requieren mantenimiento.
    Muestra componentes cuyas horas de uso han superado el límite permitido
    y componentes que están cerca del límite (90% o más).
    """
    print("\n" + "="*60)
    print("REPORTE DE MANTENIMIENTO REQUERIDO")
    print("="*60)
    
    # Cargar componentes desde archivo separado
    componentes_dict = cargar_componentes_json()
    
    componentes_criticos = []
    componentes_alerta = []
    
    # Recopilar todos los componentes críticos y en alerta
    for i in range(len(aeronaves)):
        aeronave = aeronaves[i]
        matricula = aeronave['matricula']
        modelo = aeronave['modelo']
        
        if matricula not in componentes_dict or len(componentes_dict[matricula]) == 0:
            continue
        
        for nombre_componente, datos_componente in componentes_dict[matricula].items():
            # Componentes críticos
            if datos_componente["horas_uso"] > datos_componente["limite_horas"]:
                horas_excedidas = datos_componente["horas_uso"] - datos_componente["limite_horas"]
                componentes_criticos.append({
                    'matricula': matricula,
                    'modelo': modelo,
                    'componente': nombre_componente,
                    'horas_uso': datos_componente["horas_uso"],
                    'limite': datos_componente["limite_horas"],
                    'excedidas': horas_excedidas
                })
            
            # Componentes en alerta
            porcentaje_uso = (datos_componente["horas_uso"] / datos_componente["limite_horas"]) * 100
            if porcentaje_uso >= 90 and datos_componente["horas_uso"] <= datos_componente["limite_horas"]:
                horas_restantes = datos_componente["limite_horas"] - datos_componente["horas_uso"]
                componentes_alerta.append({
                    'matricula': matricula,
                    'modelo': modelo,
                    'componente': nombre_componente,
                    'horas_uso': datos_componente["horas_uso"],
                    'limite': datos_componente["limite_horas"],
                    'porcentaje': porcentaje_uso,
                    'restantes': horas_restantes
                })
    
    # Mostrar componentes críticos
    if componentes_criticos:
        print("\nCOMPONENTES CON MANTENIMIENTO INMEDIATO REQUERIDO:")
        print("-" * 60)
        for item in componentes_criticos:
            print(f"\nCRÍTICO - Aeronave: {item['matricula']} ({item['modelo']})")
            print(f"  Componente: {item['componente']}")
            print(f"  Horas de uso: {item['horas_uso']} horas")
            print(f"  Límite permitido: {item['limite']} horas")
            print(f"  Horas excedidas: {item['excedidas']} horas")
    
    # Mostrar componentes en alerta
    if componentes_alerta:
        print("\n\nCOMPONENTES EN ALERTA DE MANTENIMIENTO:")
        print("-" * 60)
        for item in componentes_alerta:
            print(f"\nALERTA - Aeronave: {item['matricula']} ({item['modelo']})")
            print(f"  Componente: {item['componente']}")
            print(f"  Horas de uso: {item['horas_uso']} horas ({item['porcentaje']:.1f}%)")
            print(f"  Límite permitido: {item['limite']} horas")
            print(f"  Horas restantes hasta límite: {item['restantes']} horas")
    
    # Resumen final
    print("\n" + "="*60)
    if componentes_criticos:
        print(f"CRÍTICO: Se encontraron {len(componentes_criticos)} componente(s) que requieren MANTENIMIENTO INMEDIATO.")
    if componentes_alerta:
        print(f"ALERTA: Se encontraron {len(componentes_alerta)} componente(s) en alerta (90% o más de uso).")
    if not componentes_criticos and not componentes_alerta:
        print("ESTADO OK: Todas las aeronaves están en buen estado. No hay alertas.")
    print("="*60)


def mostrar_resumen_sistema(aeronaves):
    """
    Muestra un resumen general del sistema con información de todas las aeronaves
    y sus componentes registrados, incluyendo porcentaje de uso.
    """
    print("\n" + "="*60)
    print("RESUMEN DEL SISTEMA")
    print("="*60)
    
    # Cargar componentes desde archivo separado
    componentes_dict = cargar_componentes_json()
    
    # Mostrar información de aeronaves
    for i in range(len(aeronaves)):
        aeronave = aeronaves[i]
        matricula = aeronave['matricula']
        
        print(f"\n{i + 1}. Aeronave: {matricula}")
        print(f"   Modelo: {aeronave['modelo']}")
        print(f"   Horas de vuelo: {aeronave['horas_vuelo']}")
        
        # Obtener componentes de esta aeronave
        if matricula in componentes_dict:
            componentes = componentes_dict[matricula]
            print(f"   Componentes registrados: {len(componentes)}")
            
            # Mostrar componentes
            numero = 1
            for nombre_componente, datos_componente in componentes.items():
                porcentaje_uso = (datos_componente["horas_uso"] / datos_componente["limite_horas"]) * 100
                
                # Determinar estado del componente
                if datos_componente["horas_uso"] > datos_componente["limite_horas"]:
                    estado = "[CRÍTICO]"
                elif porcentaje_uso >= 90:
                    estado = "[ALERTA]"
                else:
                    estado = "[OK]"
                
                print(f"      {numero}. {nombre_componente} {estado}")
                print(f"         Horas de uso: {datos_componente['horas_uso']} / {datos_componente['limite_horas']} ({porcentaje_uso:.1f}%)")
                numero += 1
        else:
            print("   Componentes registrados: 0")


def calcular_procentaje_uso(horas_uso, limite_horas):
    """
    Calcula el porcentaje de uso de un componente.
    """
    if limite_horas == 0:
        return 0
    return (horas_uso / limite_horas) * 100


def componente_requiere_mantenimiento(horas_uso, limite_horas):
    """
    Determina si un componente requiere mantenimiento inmediato.
    """
    return horas_uso > limite_horas


def componente_en_alerta(horas_uso, limite_horas):
    """
    Determina si un componente está en estado de alerta (90% o más).
    """
    porcentaje = calcular_procentaje_uso(horas_uso, limite_horas)
    return porcentaje >= 90 and horas_uso <= limite_horas

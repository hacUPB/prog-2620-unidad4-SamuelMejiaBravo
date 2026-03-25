from datos import cargar_datos, guardar_datos

# Cargar datos al iniciar
aeronaves = cargar_datos()


def registrar_aeronave():
    print("\n--- Registro de Aeronave ---")
    matricula = input("Ingrese la matrícula (ej. HK-4532): ")
    modelo = input("Ingrese el modelo (ej. A320): ")

    while True:
        try:
            horas_vuelo = int(input("Horas de vuelo: "))
            break
        except ValueError:
            print("Ingrese un número válido.")

    aeronave = {
        'matricula': matricula,
        'modelo': modelo,
        'horas_vuelo': horas_vuelo,
        'componentes': []
    }

    aeronaves.append(aeronave)
    guardar_datos(aeronaves)

    print(f"Aeronave {matricula} registrada.")


def registrar_componente():
    print("\n--- Registro de Componente ---")

    if not aeronaves:
        print("No hay aeronaves registradas.")
        return

    matricula = input("Ingrese la matrícula: ")

    aeronave_encontrada = None
    for aeronave in aeronaves:
        if aeronave['matricula'] == matricula:
            aeronave_encontrada = aeronave
            break

    if not aeronave_encontrada:
        print("Aeronave no encontrada.")
        return

    nombre = input("Nombre del componente: ")

    while True:
        try:
            horas_uso = int(input("Horas de uso: "))
            break
        except ValueError:
            print("Número inválido.")

    while True:
        try:
            limite = int(input("Límite de horas: "))
            break
        except ValueError:
            print("Número inválido.")

    componente = {
        'nombre': nombre,
        'horas_uso': horas_uso,
        'limite': limite
    }

    aeronave_encontrada['componentes'].append(componente)
    guardar_datos(aeronaves)

    print("Componente registrado.")


def consultar_mantenimiento():
    print("\n--- Reporte de Mantenimiento ---")

    if not aeronaves:
        print("No hay aeronaves registradas.")
        return

    hay_alertas = False

    for aeronave in aeronaves:
        for componente in aeronave['componentes']:
            uso = componente['horas_uso']
            limite = componente['limite']

            if uso >= limite:
                if not hay_alertas:
                    print("\n MANTENIMIENTO INMEDIATO:")
                    hay_alertas = True

                print(
                    f"Aeronave {aeronave['matricula']} ({aeronave['modelo']}): "
                    f"{componente['nombre']} → {uso}/{limite}"
                )

            elif uso >= (0.9 * limite):
                if not hay_alertas:
                    print("\n PRÓXIMO A MANTENIMIENTO (90%):")
                    hay_alertas = True

                print(
                    f"Aeronave {aeronave['matricula']} ({aeronave['modelo']}): "
                    f"{componente['nombre']} → {uso}/{limite}"
                )

    if not hay_alertas:
        print("Todo en orden.")
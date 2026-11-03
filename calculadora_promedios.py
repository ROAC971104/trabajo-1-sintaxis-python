import re


def ingresar_calificaciones():
    materias = []
    calificaciones = []
    validador_de_nombre = r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü0-9]+(?:[ \-'][A-Za-zÁÉÍÓÚáéíóúÑñÜü0-9]+)*"

    while True:
        materia = input("Ingrese el nombre de la materia: ").strip()

        if not materia:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue

        if not re.fullmatch(validador_de_nombre, materia):
            print("Nombre inválido. Use letras, números y espacios.")
            continue

        if materia.lower() in [m.lower() for m in materias]:
            print("Esa materia ya fue ingresada. Intente con otra.")
            continue

        try:
            calificacion = float(input("Ingrese la calificación (0-10): "))
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
            continue

        if calificacion < 0 or calificacion > 10:
            print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
            continue

        materias.append(materia)
        calificaciones.append(calificacion)

        if input("¿Desea ingresar otra calificación? (s/n): ").lower().strip() != "s":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []
    for i, c in enumerate(calificaciones):
        if c >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    return calificaciones.index(max(calificaciones)), calificaciones.index(min(calificaciones))


def main():
    materias, calificaciones = ingresar_calificaciones()
    
    if not materias:
        print("No se ingresó ninguna materia.")
        print("¡Hasta luego!")
        return

    print("\n--- Resumen ---")
    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]}")

    print(f"Promedio general: {calcular_promedio(calificaciones)}")

    aprobadas, reprobadas = determinar_estado(calificaciones)
    nombres_aprobadas = [materias[i] for i in aprobadas]
    nombres_reprobadas = [materias[i] for i in reprobadas]
    print(f"Materias aprobadas: {', '.join(nombres_aprobadas) if nombres_aprobadas else 'N/A'}")
    print(f"Materias reprobadas: {', '.join(nombres_reprobadas) if nombres_reprobadas else 'N/A'}")

    maximo, minimo = encontrar_extremos(calificaciones)
    print(f"Materia con la mejor calificación: {materias[maximo]} ({calificaciones[maximo]})")
    print(f"Materia con la peor calificación: {materias[minimo]} ({calificaciones[minimo]})")
    print("¡Hasta luego!")


if __name__ == "__main__":
    main()

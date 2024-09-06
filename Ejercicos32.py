# Función para calcular el promedio de una lista de calificaciones
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para mostrar todos los alumnos y sus promedios
def mostrar_todos_alumnos(alumnos):
    print("\nLista de todos los alumnos y sus promedios:")
    for alumno in alumnos:
        nombre = alumno[0]
        calificaciones = alumno[1]
        promedio = calcular_promedio(calificaciones)
        print(f"{nombre}: {promedio:.2f}")

# Función para filtrar alumnos con promedio mayor o igual a un valor
def filtrar_promedio_mayor(alumnos, valor):
    print(f"\nAlumnos con promedio mayor o igual a {valor}:")
    for alumno in alumnos:
        nombre = alumno[0]
        calificaciones = alumno[1]
        promedio = calcular_promedio(calificaciones)
        if promedio >= valor:
            print(f"{nombre}: {promedio:.2f}")

# Función para filtrar alumnos con promedio menor a un valor
def filtrar_promedio_menor(alumnos, valor):
    print(f"\nAlumnos con promedio menor a {valor}:")
    for alumno in alumnos:
        nombre = alumno[0]
        calificaciones = alumno[1]
        promedio = calcular_promedio(calificaciones)
        if promedio < valor:
            print(f"{nombre}: {promedio:.2f}")

# Lista para almacenar los registros de los alumnos (nombre y calificaciones)
alumnos = []

# Ciclo para registrar alumnos
while True:
    nombre = input("\nIngrese el nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    calificaciones = list(map(float, input(f"Ingrese las calificaciones de {nombre} separadas por espacio: ").split()))
    alumnos.append((nombre, calificaciones))

# Mostrar todos los alumnos y sus promedios
mostrar_todos_alumnos(alumnos)

# Filtrar alumnos por promedio
valor_filtro = float(input("\nIngrese un valor para filtrar alumnos por promedio: "))
filtrar_promedio_mayor(alumnos, valor_filtro)
filtrar_promedio_menor(alumnos, valor_filtro)
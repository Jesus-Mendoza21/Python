#1
def saludos ():
    print("Hola bienvenido a la clase de phyton")

resultado = saludos ()
print("el valor retornadom por la funcion es " , resultado)
#¿Qué valor imprime la función saludo() en la consola? 
#el valor resultado
#¿Qué valor muestra la variable resultado después de ejecutar la función saludo()? 
#print
#¿Por qué la función no regresó un valor explícito? 
#porque es una funcion retornable




#2
def registrar_asistencia(estudiantes_presentes):
    print("Lista de estudiantes presentes:")
    for estudiante in estudiantes_presentes:
        print(f"- {estudiante}")

# Lista de estudiantes presentes
estudiantes_presentes = ["Ana", "Luis", "María", "Carlos", "Elena"]

# Llamada a la función para registrar la asistencia
registrar_asistencia(estudiantes_presentes)




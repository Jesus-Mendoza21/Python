#ejercicio 1
#uso de instruccion open()
archivo = open("notas.txt", "w")

archivo.write(' \n hola a todos')
archivo.write(' \n como estan ') 

#uso de close()
archivo.close()

#agregamos nuevas notas
archivo = open("notas.txt", "a")

nuevanota = ['\n en estas notas las utilizo para realizar mi actividad', '\n gracias por su atencion']

#usamos el metodo writelines 

archivo.writelines(nuevanota)

#utilizamos close
archivo.close()


#ejercicio 2

# Lista de nombres
nombres = ["Ana", "Carlos", "María", "Luis", "Elena"]

# Abrir el archivo 'nombres.txt' en modo escritura
with open("nombres.txt", "w") as archivo:
    # Recorrer cada nombre en la lista
    for nombre in nombres:
        # Escribir el nombre en el archivo, seguido de un salto de línea
        archivo.write(nombre + "\n")

print("Nombres escritos en el archivo 'nombres.txt'.")

archivo.close()


#ejercicio 3
import csv

# Lista de productos con nombre, precio y cantidad
productos = [
    ["Nombre", "Precio", "Cantidad"],  # Encabezados del archivo CSV
    ["Manzanas", 0.5, 10],
    ["Naranjas", 0.75, 20],
    ["Plátanos", 0.6, 15],
]

# Crear el archivo CSV y escribir los datos
with open('productos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(productos)

print("El archivo 'productos.csv' se ha creado correctamente.")


#ejercicio 4
try:
    # Intentar escribir en un archivo
    with open('datos.txt', 'w') as archivo:
        archivo.write("Este es un ejemplo de escritura en un archivo.\n")
    print("El archivo se ha escrito correctamente.")

except FileNotFoundError:
    # Error si el archivo no se encuentra
    print("Error: No se pudo encontrar el archivo.")

except PermissionError:
    # Error si no se tienen permisos para escribir en el archivo
    print("Error: No tienes permisos para escribir en este archivo.")

except Exception as e:
    # Cualquier otro error general
    print(f"Ha ocurrido un error inesperado: {e}")




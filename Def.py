#Ejercicio 1 
def mifuncion (nombre):
    print ('Hola')
    print (f'Hola,como estas, {nombre}')

mifuncion ('jesus')


#ejercicio 2
import math
def area_circulo(radio):
    area = math.pi * radio ** 2
    return area
radio = float(input("Proporciona un numero:"))
area = area_circulo(radio)
print(f'El resultado es: {area}')


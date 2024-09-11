#creando un diccionario 
diccionario = {
    #clave y valor 
    'IDE' : 'Integreted Development Enviroment' ,
    'OOP' : 'object Oriented Programing' , 
    'DBMS': 'Database Managment System'
}

print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento (clave)
print(diccionario['IDE'])
print(diccionario.get ('OOP'))
#modificar elemento
diccionario ['OOP'] = 'Obejct Oriented Programing'
print(diccionario)

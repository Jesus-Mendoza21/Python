#Elaborar una lista de numeros (7 numeros en la lista)
#y modificar dos elementos de esta lista 
numeros =['1','2','3','4','5','6','7']
print(numeros)
#numeros modificables 2 y el 5
numeros [2] = '10'
print(numeros)
numeros [5] = '25'
print(numeros)



#elabora una listas de frutas de tu gusto 
# y que el ususario pueda cambiar una de las frutas las cuales es de 
# y que se guarde en una lsita nueva

lista_de_frutas = ['manzana','pera','papaya','sandia',]
print(lista_de_frutas)
Fruta = (input("Cambia una fruta: "))
#lista nueva
Lista_nueva = [Fruta]
lista_de_frutas [2] = 'granada'
print(lista_de_frutas)


#realiza una lista que contenga elementos de diferentes tipos 
#y un valor boleano
#y con un for pueda mostrar lo que contiene

numeros_diferentes = ['10','12','43','54','8']
print(numeros_diferentes)
for num in numeros_diferentes:
    print(num)
    


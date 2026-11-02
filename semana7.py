#Ejemplo de colecciones en Python
#Listas
#tupla
#conjuntos
#Diccionarios

#ejemplo de lista son odenados y poermiten elementos duplicados

mi_lista = [1, 1.0, "hola", 4 + 5j]

for i in mi_lista:
    print(f"{i:6} - Tipo: {type(i)}") #esto indica el tipo de dato que es cada elemento de la lista

#se pude usar len para saber el tamaño de la lista

print(f"El tamaño de la lista es: {len(mi_lista)}")

# tambien se puede pedir que mueste algunos valores

sin_dos = mi_lista[:2] + mi_lista[3:] #esto indica que se muestre desde el indice 1 hasta el 3, pero no incluye el 3

print(mi_lista, sin_dos) #esto indica que se muestre la lista original y la lista sin el elemento 2

duplicados = mi_lista * 2 #esto indica que se duplique la lista
print(f"Lista duplicada: {duplicados}")

cuadrados = [0, 1, 4, 9, 16, 25]
#for i in range(len(cuadrados)):
#    print(f"{i}**2 = {cuadrados[i]}") #esto indica que se muestre el cuadrado de cada elemento de la lista


# tambien podemos realizar 

for i in range(len(cuadrados)):
    cuadrados[i] = cuadrados[i] ** i #esto indica que se eleve al cuadrado cada elemento de la lista
    print(f"ahora esta al cubo: {cuadrados[i]}") #esto indica que se muestre el cubo de cada elemento de la lista

cuadrados.append(7 ** 3) 



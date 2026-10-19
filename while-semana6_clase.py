print("Imprime menor a 10")
x= 1
while x < 10:
    print(x)
    x += 2


#Segundo ejemplo de while 

factorial = 5
contador = factorial - 1
while contador > 0:
    factorial *= contador
    contador -= 1
print(f"El factorial de 5 es {factorial}")

#primer ejemplo for
for i in 1, 2, 3 :
    print(i)
for i in range(3): # range se utiliza para generar una secuencia de números, en este caso del 0 al 2
    print(i)

#Segundo ejemplo for
for i in ["Ivan", "Maria", "Patricia", "Juan", "Pedro"]:
    print(i)

#tercer ejemplo for
for i in "Hola Mundo":
    if i == "M":
        pass
    else : 
        print(i, end="")
# reto de la semana 6


for i in range(2, 100):
    primo = True
    for j in range(2, i):
        if i == j :
            break
        elif i % j == 0:
            primo = False
        else:
            continue
    if primo == True:
        print(i, end=" ")
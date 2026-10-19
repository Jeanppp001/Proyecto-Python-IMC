#Ingresa el nombre de un animal 

animal = input("Ingrese el nombre del animal: ")
if animal == "perro":
    print("Guau guau")
elif animal == "gato":
    print("Miau miau")
else: print("No conozco su sonido") 
print("Conozco poco animales")

#uso de while para repetir el programa hasta que el usuario ingrese un animal que conozca
print("Impares menores a 10")
x = 1

while x <= 10:
    print(x)
    x+=2


#otro ejemplo con while para repetir el programa hasta que el usuario ingrese un animal que conozca

factorial = 5
contador = factorial - 1
while contador > 0:
    factorial *= contador
    contador -= 1
print(f"El factorial de {factorial} es {factorial}")

# como usar la sentencia for

for i in 1,2,3,4,5:
    print(i)

#Reto de la semana 5 

#la persona introduce su edad si la edad = 0 indiacara que su edad 
#no es valida va a la caja de la derecha e indicara que su edad no es valida 
# si su edad es mayor a 0 y menor a 18 indicara que es menor de edad y va a la caja de la izquierda
# si su edad es mayor a 18 y menor a 60 indicara que es adulto

entrada = input ("Ingrese su edad: ")
edad = 0

if entrada.isnumeric():
    edad = int(entrada)
else :
    print("Dato incorrecto, por favor ingrese un numero")
    exit()
if edad <= 0:
    print("hooo que joven eres pero lo siento, Edad no valida")
elif edad > 115:
    print("Vaya no creo seas tan viejo, Edad no valida")
elif edad < 18:
    print("Eres menor de edad, por favor dirijase a la caja de la izquierda")
else :
    print("Eres adulto, por favor dirijase a la caja de la derecha")
    

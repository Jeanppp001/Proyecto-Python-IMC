#texto_variado = 'palabra 123 /*-+'

#print (type(texto_variado))

# podemos utilizar comillas triple para que el texto se muestre como la cadena que hemos escrito el backslash \ se usa para agregar un salto de linea en la cadena de texto, si no se usa el backslash \ el texto se mostrara en una sola linea

#print(""" 
#funcionamiento de \
#programa: (opciones)
#    -1 Para acceder a opcines
#        -2 para salir 
# """)
###########################################################################################################################
# Subscripcion e indexado

#texto = 'Python'

#print(texto[0])
#print(texto[5])     
#print(texto[-1])
#print(texto[-6])
#print(texto[-7])


#############################################################################################################################

#letra = texto[0]
#print(letra)

# texto[0] = 'p' # esto no se puede hacer ya que las cadenas de texto son inmutables, es decir no se pueden modificars


#letra = 'p'
#print(letra)

#texto_compuesto = letra + texto[1] # concatenacion podemos unir cadenas de texto, en este caso estamos uniendo la letra 'p' con la letra 'y' que es el segundo caracter de la cadena de texto 'Python'
#print(texto_compuesto)  

###############################################################################################################################
# Slicing o substringing

#texto = 'Python'
#print(texto[0:3]) # esto nos mostrara los caracteres desde el indice 0 hasta el indice 3, es decir nos mostrara 'Pyt'
#print(texto[0:-3]) # esto nos mostrara los caracteres desde el indice 0 hasta el indice -3, es decir nos mostrara 'Pyt'
#print(texto[0:-2]) # esto nos mostrara los caracteres desde el indice 0 hasta el indice -2, es decir nos mostrara 'Pyth'
#print(texto[2:]) # esto nos mostrara los caracteres desde el indice 2 hasta el final de la cadena de texto, es decir nos mostrara 'thon'
#print(texto[:3]) # esto nos mostrara los caracteres desde el indice 0 hasta el indice 3, es decir nos mostrara 'Pyt'
#print(texto[-3::-1]) # esto nos mostrara los caracteres desde el indice -3 hasta el inicio de la cadena de texto, es decir nos mostrara 'htyP'
#print(texto[::-1]) # esto nos mostrara los caracteres desde el final de la cadena de texto hasta el inicio de la cadena de texto, es decir nos mostrara 'nohtyP'
#print(texto[1:50]) # esto nos mostrara los caracteres desde el indice 1 hasta el indice 50, es decir nos mostrara 'ython' ya que la cadena de texto 'Python' tiene solo 6 caracteres y no hay caracteres en el indice 50
#print(textgo[2:2]) # esto nos mostrara una cadena vacia ya que estamos pidiendo los caracteres desde el indice 2 hasta el indice 2, es decir no hay caracteres entre estos dos indices

#################################################################################################################################

#cadena y formato

#texto = 'hola mundo! Buenas tardes'
#print(texto.lower()) # esto nos mostrara la cadena de texto en minusculas, es decir nos mostrara 'hola mundo! buenas tardes'
#print(texto.upper()) # esto nos mostrara la cadena de texto en mayusculas, es decir nos mostrara 'HOLA MUNDO! BUENAS TARDES'
print(texto.capitalize()) # esto nos mostrara la cadena de texto con la primera letra en mayuscula y el resto en minusculas, es decir nos mostrara 'Hola mundo! buenas tardes'
#print(texto.title()) # esto nos mostrara la cadena de texto con la primera letra de cada palabra en mayuscula y el resto en minusculas, es decir nos mostrara 'Hola Mundo! Buenas Tardes'   
#print(texto.swapcase()) # esto nos mostrara la cadena de texto con las letras en mayusculas y minusculas invertidas, es decir nos mostrara 'HOLA MUNDO! bUENAS TARDES's

#texto = texto.upper() # esto nos mostrara la cadena de texto en mayusculas, es decir nos mostrara 'HOLA MUNDO! BUENAS TARDES'
#print(texto)

print('{}+{}+{}'.format(1,2,2+3)) # esto nos mostrara la cadena de texto '1+2+5' ya que estamos utilizando el metodo format para formatear la cadena de texto y estamos pasando los valores 1, 2 y 5 como argumentos
print('{}+{}+{}'.format('hola', 'mundo', 'hola mundo')) # esto nos mostrara la cadena de texto 'hola+mundo+hola mundo' ya que estamos utilizando el metodo format para formatear la cadena de texto y estamos pasando los valores 'hola', 'mundo' y 'hola mundo'como argumentos
print('{:.3f}+{:.4f} = {}'.format(2,3,2+3)) # esto nos mostrara la cadena de texto '2.000+3.0000 = 5' ya que estamos utilizando el metodo format para formatear la cadena de texto y estamos pasando los valores 2, 3 y 5 como argumentos y estamos indicando que queremos mostrar 3 decimales para el primer valor y 4 decimales para el segundo valor
print('{1}+{0}={2}'.format(2,3,2+3)) # esto nos mostrara la cadena de texto '3+2=5' ya que estamos utilizando el metodo format para formatear la cadena de texto y estamos pasando los valores 2, 3 y 5 como argumentos y estamos indicando que queremos mostrar el segundo valor primero y el primer valor despues
print('{2}+{0}={1}'.format('hola', 'mundo', 'hola mundo')) # esto nos mostrara la cadena de texto 'hola mundo+hola= mundo' ya que estamos utilizando el metodo format para formatear la cadena de texto y estamos pasando los valores 'hola', 'mundo' y 'hola mundo' como argumentos y estamos indicando que queremos mostrar el tercer valor primero, el primer valor despues y el segundo valor al final
print('{:d}={:b}={:o}={:x}'.format(15, 15, 15, 15)) # esto nos mostrara la cadena de texto '15=1111=17=f' ya que estamos utilizando el metodo format para formatear la cadena de texto y estamos pasando los valores 15, 15, 15 y 15 como argumentos y estamos indicando que queremos mostrar el primer valor en decimal, el segundo valor en binario, el tercer valor en octal y el cuarto valor en hexadecimal

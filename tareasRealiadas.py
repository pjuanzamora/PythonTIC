#Lectura y escritura por salida estandar
#Condicionales if else
#Bucles while
#Ejercicios 1-5 y 15
#Try - Except
#Números aleatorios -- Ejercicio refuerzo 1
#Números aleatorios 2 -- Funciones en Python range -- Bucle For
#Ejercicios 5 - 6 - 7 - 8 del pdf Bucles
#Listas
#Cadenas de caracteres. 
#Ejercicios cadena de caracteres. Continue y Break
#Ficheros de texto -> Lectura y Escritura. linea.split(sep)

nombre = "   Juan   Francisco fue a juan casa"
cont = 0

nombre = nombre.strip() #Eliminar espacios en blanco del principio y final
tam = len(nombre)   #Tamaño de la cadena

for i in nombre:   #Recorrer una cadena caracter a caracter
    if (i=="a"):
        cont+=1

nombre = nombre.upper() #Pasar a mayusculas
print(nombre)
nombre = nombre.lower() #Pasar a minusculas
    
#Ejercicio Buscar una palabra en un texto
#Contar cuantas veces aparece

buscar = input("Dime una palabra para buscarla: ")
texto = "lorjuan em ipsum juan pepe siiii juan asdfasf "
cont=0
while (texto.find(buscar) != -1):
    cont += 1
    texto = texto[texto.find(buscar)+1:]

print(cont)
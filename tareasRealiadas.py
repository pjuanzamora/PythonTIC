#Lectura y escritura por salida estandar
#Condicionales if else
#Bucles while
#Ejercicios 1-5 y 15
#Try - Except
#Números aleatorios -- Ejercicio refuerzo 1
#Números aleatorios 2 -- Funciones en Python range -- Bucle For
#Ejercicios 5 - 6 - 7 - 8 del pdf Bucles
#Listas



vNum = []
num = 0

while num != -1:
    num = int(input("Dame un numero: \n"))
    if (num != -1):
        vNum.append(num)


print ("Los números leidos son: ", len(vNum), " y son: ", vNum)
print ("El mayor es: ", max(vNum))
print ("El menor es: ", min(vNum))





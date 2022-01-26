#Lectura y escritura por salida estandar
#Condicionales if else
#Bucles while
#Ejercicios 1-5 y 15
#Try - Except
#Números aleatorios -- Ejercicio refuerzo 1

import random

jugar = "s"
while jugar == "s":
    aleatorio = random.randint(0,10)
    seleccion = -1
    intentos = 0
    bandera = True
    while seleccion != aleatorio:

    #Bloque para leer un número sin fallos
        while bandera: 
            try:
                seleccion = (int)(input("Dame un número "))
                bandera = False
            except:
                print("Un NÚMERO MELÓN")
    #Fin leer un número sin fallos, pongo la bandera de nuevo a True
        bandera = True
    #Doy pista si es mayor o menor
        if (seleccion < aleatorio):
            print("El número es mayor")
            intentos += 1
        elif (seleccion > aleatorio):
            print("El número es menor")
            intentos += 1

    #Fin del programa
    print("Felicidades! Has adivinado el número ", aleatorio,  "en ", intentos, "intentos")
    jugar = input("¿Quieres volver a jugar? s/n")


#Ejercicios 1.4

'''Ejercicios 1

palabra = input("Dime una palabra: ")
tam = len(palabra)-1

while (tam>=0):
    print(palabra[tam],end="")
    tam-=1

'''

'''Ejercicio 2

'''
def imprimeConMayusculas(texto):
   
    texto = texto.lower()
    bandera=True
    for i in texto:
        if bandera:
            print(i.upper(),end="")
        else:
            print(i,end="")
        bandera = not(bandera)

    return bandera


texto = input("Dime una palabra: ")
print(imprimeConMayusculas(texto))

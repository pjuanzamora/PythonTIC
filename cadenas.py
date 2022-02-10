#Ejercicios 1.4

'''Ejercicios 1

palabra = input("Dime una palabra: ")
tam = len(palabra)-1

while (tam>=0):
    print(palabra[tam],end="")
    tam-=1

'''

'''Ejercicio 2
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
'''

'''Ejercicio 3
palabra = input ("Dime una palabra ")
cont=0
for i in palabra:
    if i in ("a","e","i","o","u"):
        cont+=1
print("Hay",cont, "vocales")
'''


'''Ejercicio 4
palabra = input ("Dime una palabra ")
vocales = ["a","e","i","o","u"]

for i in vocales:
    for j in palabra:
        if i==j:
            print(i,end=" ")
            break
'''

'''Ejercicio 5

'''

texto = input ("Dime una palabra ")

tam = len(texto)-1
cont=1
i=0
while i<tam:
    if (texto[i] == " " and texto[i+1]!=" "):
        cont+=1
    i+=1

print(cont)
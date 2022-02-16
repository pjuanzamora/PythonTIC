#Lectura de ficheros de texto

from encodings import utf_8

with open("datos.txt","r",encoding="utf_8") as fdatos:
    for linea in fdatos:
        print(linea)
'''

try:
    fdatos = open("datos.txt",encoding="utf_8")
except:
    fdatos = open("datos.txt",'w')
    fdatos.close()
    fdatos = open("datos.txt","r")


for linea in fdatos:
    print(linea)

fdatos.close()
'''

#Escritura de ficheros de texto

fdatos = open("nombres.txt", "a")

fdatos.write("\nJuan\nPepe\nJose")

fdatos.close()


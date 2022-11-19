#ABRINDO UN ARCGIVO CSV DE FORMA CORRECTA 
import csv

ruta_de_correos = input("¿Cual es la ruta de archivo de los correos? ")

lista_de_correos = []

with open(ruta_de_correos) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        printe = (', '.join(row))
        lista_de_correos.append(printe)
print(lista_de_correos)
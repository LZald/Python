import os
from Vehiculos import Coche

pathBase = os.path.dirname(os.path.abspath(__file__))

listaCoches = []

def menu():
    print('\n1 - Introducir Coche')
    print('\n2 - Salir\n')
    return int(input())

def introCoche():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    color = input("Color: ")
    coche = Coche(marca, modelo, color)
    return coche

def cargaCoches():
    with open(f'{pathBase}/coches.txt', 'r', encoding = 'UTF-8') as archivo:
        for f in archivo:
            listaCoches.append(f[:-1])

def saveCoche(coche):
    listaCoches.append(coche)
    with open(f'{pathBase}/coches.txt', 'a', encoding = 'UTF-8') as archivo:
        archivo.write(str(coche) + '\n')

cargaCoches()

while menu() == 1:
    # listaCoches.append(introCoche())
    # print("Lista de coches:\n", listaCoches)
    saveCoche(introCoche())

print(listaCoches)


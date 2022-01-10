#Probando que todo esto funcione

import os
import time
from Vehiculos import Coche

pathBase = os.path.dirname(os.path.abspath(__file__))

coches = []

with open(f'{pathBase}/coches.txt', 'r', encoding = 'UTF-8') as archivo:
    data = archivo.read()
data = data.split("\n")

for coche_str in data:
    values = coche_str.split(';') 
    if len(values) > 2:
        car = Coche(values[0], values[1], values[2])
        values = values[3:]
        for val in values:
            car.caract.append(val)
        coches.append(car)

print(coches)
exit(0)

# Opcion 1
# while True:
#     coche = {}
#     coche['marca'] = input("Marca: ")
#     coche['modelo'] = input("Modelo: ")
#     coche['color'] = input("Color: ")

#     with open(f'{pathBase}/coches.txt', 'a', encoding = 'UTF-8') as archivo:
#         archivo.write(f"{coche['marca']} {coche['modelo']} {coche['color']}\n")
    
#     continuar = input('Continuar?: ')
#     if continuar.lower() not in ['y','yes','si', 's']:
#         break

#opcion 2
while True:
    coche = Coche(None, None, None)
    coche.marca = input("Marca: ")
    coche.modelo = input("Modelo: ")
    coche.color = input("Color: ")

    with open(f'{pathBase}/coches.txt', 'a', encoding = 'UTF-8') as archivo:
        archivo.write(f"{coche.export()}\n")

    continuar = input('Continuar?: ')
    if continuar.lower() not in ['y','yes','si', 's']:
        break




# --------------------------------   Contador de tiempo de ejecución
# start_time = time.time()
# a = 0
# while a<10000000:
#     a+=1
# print("--- %s seconds ---" % (time.time() - start_time))

print("Bye")

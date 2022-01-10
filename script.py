# import calculadora
# print(calculadora.suma(3,5))

# or

# import calculadora as clc
# print(clc.suma(3,5))

# or

# from calculadora import suma, resta
# print(suma(3,5))
# print(resta(3,5))

# from Vehiculos import Vehiculo
# coche = Vehiculo("Tesla")
# print(coche.marca)
# coche.mover()

# from Vehiculos import Coche
# coche = Coche("Tesla", "Roaster")
# coche.mover()
# print(coche.modelo)

# 06/10/21

from Vehiculos import Coche

coche1 = Coche("Tesla", "Roaster")
coche2 = Coche("Ford", "Mustang")

print(coche1)

coches = [coche1, coche2]
cochesDict = {}
for car in coches:
    cochesDict[car.marca] = car

# cochesDict = dict(enumerate(set(coches)))

# cochesDict = {"Tesla": coche1, "Ford": coche2}

print(cochesDict)
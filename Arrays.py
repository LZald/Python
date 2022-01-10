
# Arrays día 1

# lista = [0,3,5,56,5,4]
# subLista = lista[4:6]

# print(lista[1:5])

# for item in lista[0:len(lista)-1]:
#     print(item, end=' - ')
# print(lista[-1])

# print(7//2)

# mitad = len(lista)//2
# if len(lista) % 2 ==0:
#     lista.insert(mitad, "medio")
# else:
#     lista[mitad] = "Medio"
# print(lista)

# for index, item in enumerate(lista):
#     print(f"{index} - {item}")

# Arrays día 2

# lista = ['cero', 'uno', 'dos', 'uno', 'tres']             #lista
# lista.append('last')
# lista.remove('uno')
# if 'cero' in lista:
#     print("Está")
# else:
#     print('No está')
# lista.pop()
# print(lista)
# lista.clear()
############################################################
# meses = ('aaa', 'bbb', 'ccc')                             #Tupla
# print(len(meses))

# for index, item in enumerate(meses):
#     print(index, item)

# lista_meses = list(meses)
# lista_meses[1] = 'Junio'
# print(lista_meses)

# meses = tuple(lista_meses)
# print(meses)
#############################################################

# meses = {'Enero', 'Febrero', 'Mazo', 'Febrero'}             #Sets
# item = meses.pop()
# print(meses)
# print(item)

#############################################################

coche = {
    'marca': 'Tesla',
    'modelo': 'Roadster 2020',
    'color': 'Negro',
    'puertas': 4,
    'ruedas': 4
}

lista_valores = list(coche.values())
lista_keys = list(coche.keys())

coche['color'] = 'Amarillo'

for cosa in coche:
    print(f"{cosa}: {coche[cosa]}")

print('-----------------------------------')
for valor in coche.values():
    print(valor)
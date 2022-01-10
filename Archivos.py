# import os

# print('-----\n', os.getcwd(), '\n-----')
# print(os.path.dirname(os.path.abspath(__file__)))

# with open('datos.txt', 'r') as archivo:
#     texto = archivo.read()

# with open('datos.txt', 'a') as archivo:
#     archivo.write('\nOtra cosa')

# with open('datos.txt', 'a', encoding = 'UTF-8') as archivo:
#     archivo.write('\nOtra cosa')

# with open('datos2.txt', 'w') as archivo:
#     archivo.write('Datos de otro lado')

# print(texto)

#                           Usar ruta relativa pero absoluta 
# import os
# pathBase = os.path.dirname(os.path.abspath(__file__))

# with open(f'{pathBase}/datos.txt', 'a', encoding = 'UTF-8') as archivo:
#     archivo.write('\nOtra cosa')


#                           Cosas de leer archivo
# import os

# pathBase = os.path.dirname(os.path.abspath(__file__))

# with open(f'{pathBase}/datos.txt', 'r', encoding = 'UTF-8') as archivo:
#     line = archivo.readline()
#     while line:
#         line = archivo.readline()
#         print(line)

#                           Script sobre coches



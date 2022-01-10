# variable = 1
# variable1 = True
# variable2 = False
# numero = 12
# variable = "hola " + str(numero)
# variable = f"hola {numero*2} - {numero}"

# if variable1 and numero == 12:
#     print("Ifside")

# print(variable)

# while numero < 15:
#     print(numero)
#     numero += 1

dato = input("Ponme algo, guapa")

# print("Pusiste: " + dato)
# print(f"De tipo: {type(dato)}")
# print(f"aaa: {dato*2}")

try:
    dato = int(dato)
    if dato >= 10:
        raise Exception("Número fuera de rango")
    dato = dato/0
    print(f"Ahora int: {type(dato)}")
except ZeroDivisionError as e:               # "except" captura cualquier fallo. "except Exception" captura solo si falla algo del código
    print("No, 0 es el problema")
    print(str(e))
except ValueError as e:
    print("No, valor es el problema")
    print(str(e))
except Exception as e:
    print("No, Otra cosa es el problema")
    print(str(e))



def suma(*numeros):     ## Con * le puedes pasar el número que quieras. No le puedes pasar una lista
    res = 0
    for num in numeros:
        res += num
    return res

def factorial(numero):
    res=1
    while numero > 0:
        res *= numero
        numero -= 1
    return res

def factorial_recursivo(num):
    if num < 0:
        raise Exception( "Número no válido")
    if num == 0:
        return 1
    return num * factorial_recursivo(num-1)

print(factorial_recursivo(5))
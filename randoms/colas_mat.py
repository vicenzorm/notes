import math


def potencia(x: int, y: int):
    resultado = x ** y

    print(resultado)


def descobrir_resto(x, y):
    resultado = x // y
    resto = x % y

    print(f"O resultado: {resultado} e o resto: {resto}")


def bhaskara(a, b, c):
    delta = math.sqrt((((b) ** 2) - 4 * a * c))
    x_1 = (-(b) + delta) / (2 * a)
    x_2 = (-(b) - delta) / (2 * a)

    print(f"x1: {x_1} e x2: {x_2}")


def area_quadrado(x):
    area = x ** 2
    print(f"Area: {area}")


def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2 
        if lista[meio] == valor:
            print(f"Índice do meio: {meio}, Valor no meio: {lista[meio]}")
            break
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False


def descobrir_mediana(lista = list[int]):
    lista.sort()
    inicio = 1
    fim = len(lista) 
    meio = (inicio + fim) / 2
    if (inicio + fim) % 2 == 0:
        meios_1, meios_2 = int(meio - 1)
        #meios_2 = int(meio - 1)
        print((lista[int((meios_1 + meios_2) / 2)])) #100% Accuracy
    else:
        meios_3 = int(meio)
        meios_4 = int(meio - 1)
        print((lista[meios_3] + lista[meios_4]) / 2) #100% Accuracy



def media(lista = list[int]):
    quantidade = len(lista)
    soma = 0
    for i in lista: 
        soma = soma + i
    resultado = soma / quantidade
    print(resultado)


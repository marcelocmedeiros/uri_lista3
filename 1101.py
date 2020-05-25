# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles
(incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número
 nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2                 2 3 4 5 Sum=14
6 3                 3 4 5 6 Sum=18
5 0
'''

aux = 0
maior = 0
menor = 0

cond = True
while cond:
    valor1, valor2 = map(int, input().split())

    if (valor1 <= 0 or valor2 <= 0):
        break

    maior = valor1 if valor1 > valor2 else valor2
    menor = valor2 if valor2 < valor1 else valor1

    if maior > menor:
        aux = maior
        maior = menor
        menor = aux

    soma = 0

    while maior <= menor:
        print(maior, end=' ')
        soma += maior
        maior += 1
    print("Sum=%d" % soma)

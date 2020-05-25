# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste
de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada	Exemplo de Saída
7                       0
4 5                     11
13 10                   5
6 4                     0
3 3                     0
3 5                     0
3 4                     12
3 8
'''
# quantidade de casos de teste
n = int(input())
d = 0

for c in range(1 , n + 1):
    x = input().split()
    a, b, = x
    s=0
    a = int(a)
    b = int(b)
    # a > b faz um lação for de b para a somando os ímpares
    if a > b:
        for d in range(int(b)+1, int(a)):
            if d % 2 != 0:
                s = s + d
    # b > a faz um lação for de a para b somando os ímpares
    if a < b:
        for d in range(int(a)+1, int(b)):
            if d % 2 != 0:
                s = s + d
    # a == b não existe números ímpares entres eles s = 0
    if a == b:
        s = 0
    print(s)

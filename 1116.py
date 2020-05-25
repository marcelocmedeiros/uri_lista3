# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y)
que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel”
caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro.
Utilize cast :)

Exemplo de Entrada	Exemplo de Saída
3                       -1.5
3 -2                divisao impossivel
-8 0                    0.0
0 8
'''

# variavel de quantidade de pares quer fazer a divisão
n = int(input())
# um for para percorrer quantidade de valor "n"
for i in range(1, n + 1):
    # add os 2 valores por espaço em branco .split()
    x, y = input().split()
    # converter o "x" e "y" em inteiro
    x = int(x)
    y = int(y)
    # condição de divisão impossivel
    if y == 0:
        print('divisao impossivel')
    # mostra a divisão
    if y != 0:
        divisao = x / y
        print('{:.1f}'.format(divisao))
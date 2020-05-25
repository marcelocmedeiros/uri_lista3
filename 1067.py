# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha,
inclusive o X, se for o caso.

Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.

Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

Exemplo de Entrada	Exemplo de Saída
8                       1
                        3
                        5
                        7
                        12
'''

# ler um valor inteiro
x = int(input())
# para mostrar os valores impares de 1 até x
i = 1
while i <= x:
    # condição para ser ímpar
    if i % 2 != 0:
        print(i)
    i = i + 1
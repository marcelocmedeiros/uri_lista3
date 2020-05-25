# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada	Exemplo de Saída
7                   4 valores positivos
-5
6
-3.4
4.6
12
'''

y = 0
# for in range(1,7) para ler 6 valores
for x in range(1,7):
    a = float(input())
    # if para somar apenas os valores postivos
    if a > 0:
        # contador
        y = y + 1
print('{} valores positivos'.format(y))




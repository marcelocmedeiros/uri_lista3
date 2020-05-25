# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada	Exemplo de Saída
7                   3 valores pares
-5
6
-4
12
'''

a = []
l = 0
# ler 5 valores
for i in range(5):
    n = int(input())
    # add lista "a"
    a.append(int(n))
    #condição p ser par
    if n % 2 == 0:
        # soma se for par
        l += 1
print(l, "valores pares")

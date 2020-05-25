# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X,
um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	Exemplo de Saída
8                      9
                        11
                        13
                        15
                        17
                        19
'''

'''num = int(input())
impares = [n for n in range(num,num+12) if n % 2 != 0]
for n in impares:
    print(n)'''

# lista vazia p receber 6 valores ímapres
lista = []
num = int(input())
n = num
# for para ir num até num + 12 valores para encontrar todos os ímpares
for n in range(num,num+12):
    # condição p ser ímpar
    if n % 2 != 0:
        # add a lista
        lista.append(n)
# imprime da forma indicada na saída
for c in lista:
    print(c)

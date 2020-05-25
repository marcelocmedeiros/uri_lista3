# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da
divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Sample Input	Sample Output
10                  12
18                  13
                    17
'''
#leia 2 valores X e Y
x = int(input())
y = int(input())
# condição de qual número é o menor, assim ele passa ser "a" e o maior "b"
if x > y:
    a = y
    b = x
# condição de qual número é o menor, assim ele passa ser "a" e o maior "b"
if x <= y:
    a = x
    b = y
a = a + 1
# laço entre que vai do menor "a" até maior "b"
while a < b:
    # condição p imprimir divisão dele por 5 == 2 ou == 3
    if a % 5 == 2 or a % 5 == 3:
        print(a)
    a = a + 1

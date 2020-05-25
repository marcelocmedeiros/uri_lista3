# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os
valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada	Exemplo de Saída
6                       5
-5

15                      13
12

12                      0
12
'''

x = int(input())
y = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor+=1
soma = 0

while (menor < maior):
    if(menor % 2 != 0):
        soma+=menor
    menor+=1
print(soma)

'''
x = int(input())
y = int(input())

# verificar qual valor é o maior e o menor
if x > y:
    maior = x
else:
    maior = y
if y < x:
    menor = y
else:
    menor = x
menor+=1
soma = 0
# loop vai do menor até maior
while (menor < maior):
    # condição p ser ímpar
    if(menor % 2 != 0):
        # soma dos ímpares como foi pedido
        soma+=menor
    menor+=1
print(soma)
'''
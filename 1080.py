# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
2                       34565
113                       4
45
34565
6
...
8
'''

x=0
# um laço a ler 100 valores
for i in range(0,100):
    a = int(input())
    # se a > x então maior = a na posição i + 1 e x == a
    if a > x:
        maior = a
        posicao = i + 1
        x = a

print(maior)
print(posicao)

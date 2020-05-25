# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N,
inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000
o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

Exemplo de Entrada	Exemplo de Saída
 6                      2^2 = 4
                        4^2 = 16
                        6^2 = 36
'''

n = int(input())
# primeiro n° par depois de 1, assim x = 2
x = 2
# usando for iniciando por 2 e saltando de 2 em 2 p continuar par até "n + 1" p receber o valor de "n"
for i in range(2 , n + 1, 2):
    print('{}^2 = {}'.format(i, i **2))

# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN),
ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0),
embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá
imprimir apenas NULL.

Entrada
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão
ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

Exemplo de Entrada	Exemplo de Saída
4                       ODD NEGATIVE
-5                      NULL
0                       ODD POSITIVE
3                       EVEN NEGATIVE
-4
'''

# variavel que vai indicar qual a quantidade de valores a serem lidos
n = int(input())
# uma lista dos valores lidos
x = ['']
# for para loop de valores a serem lidos
for i in range(1, n + 1):
    # x.append p add a lista x
    x.append(int(input()))
# 2° for para percorrer a lista e satisfazer as condições
for i in range(1, n + 1):
    # se x == 0 nulo
    if x[i] == 0:
        print('NULL')
    # se x > 0 positivo
    if x[i] > 0:
        # se positivo e par
        if x[i] % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    # se x > 0 negativos
    if x[i] < 0:
        # se negativos e par
        if x[i] % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')


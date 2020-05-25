# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando
essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).


Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

Exemplo de Entrada	Exemplo de Saída
4                       2 in
14                      2 out
123
10
-25
'''

# variável do n° de loop do for
n = int(input())
# contadores do intevalo entre [10,20] q  estão dentro e fora
dentro = 0
fora = 0
# loops da quantidade de n° a serem verificados no intevalo entre [10,20]
for i in range(0, n):
    x = int(input())
    if 10 <= x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print('{} in'.format(dentro))
print('{} out'.format(fora))

'''n = int(input())
dentro = 0
fora = 0
for i in range(1,n + 1):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print('{} in'.format(dentro))
print('{} out'.format(fora))'''
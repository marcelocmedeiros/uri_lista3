# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha,
deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes
números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos
valores positivos digitados.

Exemplo de Entrada	Exemplo de Saída
7                   4 valores positivos
-5                  7.4
6
-3.4
4.6
12
'''

t = []
# for in range(1,7) para ler 6 valores
for x in range(1,7):
    a = float(input())
    # vai add a lista t
    t.append(a)

s=0
m =0
t1 = t
for n in t1:
  if n > 0:
    s = s + 1
    m = m + (n)
print('{} valores positivos'.format(s))
print('{:.1f}'.format(m/s))
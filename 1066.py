# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores
digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final
de linha após cada uma.

Exemplo de Entrada	Exemplo de Saída
-5                  3 valor(es) par(es)
0                   2 valor(es) impar(es)
-3                  1 valor(es) positivo(s)
-4                  3 valor(es) negativo(s)
12
'''

a = []
l = 0
m = 0
o = 0
p = 0
# ler 5 valores
for i in range(5):
    n = int(input())
    # add a lista "a"
    a.append(int(n))
    # verifica se é par e soma par
    if n % 2 == 0:
        l += 1
    # verifica se é ímpar e soma ímpar
    if n % 2 == 1:
        m += 1
    # verifica se é positivo e soma positivo
    if n > 0:
        o += 1
    # verifica se é negativo e soma negativo
    if n < 0:
        p += 1
print(l, "valor(es) par(es)")
print(m, "valor(es) impar(es)")
print(o, "valor(es) positivo(s)")
print(p, "valor(es) negativo(s)")

# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral.
Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]).
Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem
lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo.
O valor deve ser apresentado com duas casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
-3.5                 nota invalida
3.5                  nota invalida
11.0                 media = 6.75
10.0
'''

#contador de n° de notas
i = 0
# somatorio de nota1 e nota2
med = 0
# laço while p as duas notas usei while pois pode ser escritas notas invalidas q não entraram no calculo da média
while i < 2:
    nota = float(input())
    # condição para nota ser valida
    if nota >= 0 and nota <= 10:
        i = i + 1
        med = med + nota
    # nota invalida e print informando
    if nota < 0 or nota > 10:
        print('nota invalida')
# media
med = med / 2
print('media = {:.2f}'.format(med))

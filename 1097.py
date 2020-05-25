# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
                        I=1 J=7
                        I=1 J=6
                        I=1 J=5
                        I=3 J=9
                        I=3 J=8
                        I=3 J=7
                        ...
                        I=9 J=15
                        I=9 J=14
                        I=9 J=13
'''
# variáveis iniciais foram informada I=1 e J=7
i = 1
j = 7
# no 1° laço do par o valor I vai até 9 saltando de 2 em 2
while i <= 9:
    # for para "J" se repetir 3 decrescendo de 1 em 1 p depois sair p while
    for c in range(0,3):
        print('I={} J={}'.format(i,j))
        # descrescendo -1
        j = j - 1
    # quando sair do for I += 2 e J +=5
    i = i + 2
    j = j + 5
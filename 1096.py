# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

Exemplo de Entrada	Exemplo de Saída
                        I=1 J=7
                        I=1 J=6
                        I=1 J=5
                        I=3 J=7
                        I=3 J=6
                        I=3 J=5
                        ...
                        I=9 J=7
                        I=9 J=6
                        I=9 J=5
'''

# variáveis iniciais foram informada I=1 e J=7
i = 1
j = 7

# no 1° laço do par o valor I vai até 9 saltando de 2 em 2
while i <= 9:
    # no 2° do par J decresce de 7 até 5 (-1) p depois sair p 1° laço
    while j >= 5:
        print('I={} J={}'.format(i,j))
        j = j - 1
    # i soma de +2 começando de 1 até chegar 9
    i = i + 2
    # J sempre começa o par com 7 e decresce até 5 no 2° laço
    j = 7

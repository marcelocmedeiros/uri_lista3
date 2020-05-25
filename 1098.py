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
                        I=0 J=1
                        I=0 J=2
                        I=0 J=3
                        I=0.2 J=1.2
                        I=0.2 J=2.2
                        I=0.2 J=3.2
                        .....
                        I=2 J=?
                        I=2 J=?
                        I=2 J=?
'''

# variáveis iniciais foram informada I=0 e J=1
i = 0
j = 1
acrescimo = (0.2)
n = 0
# no 1° laço do par o valor I vai até 2 começando do 0 e crescendo de 0.2
while i <= 2:
    # for para "J" se repetir 3 crescendo de 0.2 em cada loop p depois sair p while
    for c in range(0,3):
        if i > 2.19:
            print('I={:.0f} J={:.0f}'.format(2,j))
        if i == 1.0 or i == 0.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i,j))
        elif i < 2:
            print('I={:.1f} J={:.1f}'.format(i,j))
        j = j + 1
    i = i + acrescimo
    j = 1 + i
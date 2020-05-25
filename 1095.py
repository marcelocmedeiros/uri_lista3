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
                        I=1 J=60
                        I=4 J=55
                        I=7 J=50
                        ...
                        I=? J=0
'''

# variáveis iniciais foram informada I=1 e J=60
i = 1
j = 60
# na ultima saída "J" é igual a "0" então o laço decresce até J == 0
while j >= 0:
    # priint vem primeiro pq tem q receber os dois termos iniciais
    print('I={} J={}'.format(i,j))
    # operação vem depois do print para gerar os novos atributos de I e J p imprimir no próximo laço
    i = i + 3
    j = j - 5

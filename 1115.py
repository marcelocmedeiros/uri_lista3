# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Escreva um programa para C de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas
coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme
o exemplo.

Exemplo de Entrada	Exemplo de Saída
2 2                 primeiro
3 -2                quarto
-8 -1               terceiro
-7 1                segundo
0 2
'''


while(True):
  x, y = input().split()

  x = int(x)
  y = int(y)

  if(x == 0) or (y == 0):
    break
  elif(x > 0) and (y > 0):
    print('primeiro')
  elif(x < 0) and (y > 0):
    print('segundo')
  elif(x < 0) and (y < 0):
    print('terceiro')
  else:
    print('quarto')
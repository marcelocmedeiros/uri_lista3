# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# 3 Lista
# Patos-PB maio/2020

'''
Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

Entrada
A entrada contém um valor inteiro N (N < 10000).

Saída
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

Exemplo de Entrada	Exemplo de Saída
   13                    2
                        15
                        28
                        41
                        ...
'''

# variável q vai indicar o n° divisível q tem resto === 2 entre [1,1000]
n = int(input())
# for in range p percorer a sequencia entre [1,1000] lembrando q o ultimo tem q ser 10001
for i in range(1,10001):
    # condição de [1,1000] % n == 2
    if i % n == 2:
        print(i)

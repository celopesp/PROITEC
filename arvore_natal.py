""""
As crianças adoram desenhar árvores de natal e você desafiou algumas delas a 
desenharem árvores de diversos tamanhos com apenas com o caractere asterisco "*".

A regra é simples. De baixo para cima, o tronco da árvore consiste de 3 asteriscos e depois 1. 
Em seguida vem o restante da árvore, com cada fileira de folhas iniciando no tamanho que você determinou e 
diminuindo de dois em dois, até chegar na copa da árvore que terá apenas um asterisco. Note que para isso dar certo, 
somente será permitido tamanhos ímpares para estas árvores.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste consiste em um inteiro N (2 < N < 100).

Saída
Para cada caso de teste de entrada, seu programa deverá desenhar uma árvore conforme especificação acima e exemplo abaixo, com uma linha em branco após cada árvore.

"""
import math
valido = False
while(valido == False):
    N = int(input ("informe um inteiro N (2 < N < 100):"))
    resto = N%2
    if (N>2 and N<100 and resto>0):
        valido = True

meio_linha = math.ceil(N/2) #arredondando para cima o meio da linha

#PREENCHER QTD DE ASTERISTICOS EM CADA LINHA
espacos = meio_linha - 1
for contador in range(1, N+1, 2):
    linha_preenchida = "*" * contador
    linha_preenchida = (" " * espacos) + linha_preenchida
    print(linha_preenchida)
    espacos -= 1

#imprimindo saida do tronco base com 1 *
linha = ""
for contador in range (1, N):
    if(contador==meio_linha):
        linha += "*"
    else:
        linha += " "
print(linha)

#imprimindo saida do tronco base com 3 ***
linha = ""
for contador in range (1, N):
    if(contador==meio_linha-1 or contador==meio_linha or contador==meio_linha+1):
        linha += "*"
    else:
        linha += " "
print(linha)
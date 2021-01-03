"""César é um detetive que investiga uma série de roubos que acontecem em sua cidade. 
Em todo lugar que um crime acontece, a pessoa que cometeu tal crime deixa uma mensagem escrita, 
formada por letras maiúsculas e minúsculas. 
César conseguiu achar um padrão nestas mensagens e agora extrai um texto oculto em cada mensagem e 
pede a sua ajuda para tentar descobrir quem está cometendo tais crimes.

Entrada
A entrada é composta por vários casos de teste. 
A primeira linha contém um número inteiro C (2 <= C <= 99) relativo ao número de casos de teste. 
Nas C linhas seguintes, haverá mensagens codificadas, todas com um mesmo padrão em relação ao exemplo abaixo.

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir o texto extraído da mensagem original.
"""
valido = False
while(valido == False):
    C = int(input("digite a quantidade de palavras que deseja descriptografar:"))
    if(C>1 and C<100):
        valido = True

lista = []

for contador in range (1, C+1):
    palavra = input(f"digite a {contador}ª palavras que deseja descriptografar:")
    tamanho_palavra = len(palavra)
    palavra_ordenada = ""
    reverso = -1
    for contador_ordenar_palavra in range (tamanho_palavra-1, -1, -1):
        palavra_ordenada += palavra[reverso]
        reverso -= 1
    lista.append(palavra_ordenada)

for contador in range (0, C):
    tamanho_palavra = len(lista[contador])
    palavra = lista[contador]
    descriptografada = ""
    for aux in range(0,tamanho_palavra):
        if(palavra[aux].islower()):
            descriptografada += palavra[aux]
    print(f'descriptografada:{descriptografada}')
        

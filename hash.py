"""
Você terá como uma entrada várias linhas, cada uma com uma string. O valor de cada caracter é computado como segue:

Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento)

Todas posições são baseadas em zero. 'A' tem posição 0 no alfabeto, 'B' tem posição 1 no alfabeto, ... 
O cálculo de hash retornado é a soma de todos os caracteres da entrada. Por exemplo, se a entrada for:
CBA
DDD

então cada caractere deverá ser computado como segue:

2 = 2 + 0 + 0 : 'C' no elemento 0 posição 0
2 = 1 + 0 + 1 : 'B' no elemento 0 posição 1
2 = 0 + 0 + 2 : 'A' no elemento 0 posição 2
4 = 3 + 1 + 0 : 'D' no elemento 1 posição 0
5 = 3 + 1 + 1 : 'D' no elemento 1 posição 1
6 = 3 + 1 + 2 : 'D' no elemento 1 posição 2

O cálculo final de hash será 2+2+2+4+5+6 = 21.
"""

alfabeto = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
            'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
            'V':21,'W':22,'X':23,'Y':24,'Z':25}

N = int(input("Informe a quantidade de casos de testes (numero inteiro):"))
somatorio = 0
for contador_fora in range (0, N):
    valido = False
    while(valido == False):
        entrada = input("Informe a string para calculo do Hash:").upper()
        if(len(entrada)<51):
            valido = True
    for contador in range (0, len(entrada)):
        chave = entrada[contador]
        somatorio += alfabeto[chave] + contador + contador_fora
print(f'somatorio ={somatorio}')
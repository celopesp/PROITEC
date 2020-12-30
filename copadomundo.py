"""
Uma Copa do Mundo de futebol de botões está sendo realizada com times de todo o mundo. 

A classificação é baseada no número de pontos ganhos pelos times, e a distribuição de pontos é feita da forma usual. 
Ou seja, quando um time ganha um jogo, ele recebe 3 pontos; 
se o jogo termina empatado, ambos os times recebem 1 ponto; 
e o perdedor não recebe nenhum ponto.

Dada a classificação atual dos times e o número de times participantes na Copa do Mundo, 
sua tarefa é de determinar quantos jogos terminaram empatados até o momento.

Entrada
A entrada contém vários casos de teste. 
A primeira linha de um caso de teste contém dois inteiros T e N, 
indicando respectivamente o número de times participantes (2 ≤ T ≤ 200) e o número de partidas jogadas (0 ≤ N ≤ 10000). 

Cada uma das T linhas seguintes contém o nome de um time (uma cadeia de máximo 10 letras e dígitos), 
seguido de um espaço em branco, seguido do número de pontos que o time obteve até o momento. 

O final da entrada é indicado por T = 0.

Saída
Para cada um dos casos de teste seu programa deve imprimir uma única linha contendo um número inteiro, 
representando a quantidade de jogos que terminaram empatados até o momento.
"""

T = -1

while(T!=0):
    total_pontos = 0
    T,N = input("Insira a Qtd de Times e a Qtd de Partidas separado por espaço ((2 ≤ TIMES ≤ 200) e (0 ≤ PARTIDAS ≤ 10000)):").split()
    T = int(T)
    N = int(N)
    if((1<T<201) and (0<N<10001)):
        for qtd_times in range(0, T):
            tamanho = False
            while(tamanho!=True):
                nome_time, pontos = input(f'Insira o Nome do {qtd_times+1}° time com até 10 caracteres e a qtd de Pontos separados por espaço:').split()
                if (len(nome_time) <=10):
                    tamanho = True
                    pontos = int(pontos)
                    total_pontos += pontos
            qtd_times += 1
        empates = (N * 3) - total_pontos
        print(empates)
        #print("total de empates:", empates)
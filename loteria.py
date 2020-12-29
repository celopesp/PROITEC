"""
Flavinho sabe que a chance de ganhar na loteria é bem pequena. 
Ele gosta muito de estudar probabilidade! 
Mas, justamente por entender de probabilidades, Flavinho segue o ditado, “quem não arrisca, não petisca!”, e faz um jogo toda semana.

Na loteria preferida dele, o jogador aposta seis números entre 1 e 99. 
No sorteio, também são escolhidos seis números ganhadores entre 1 e 99. 
Quem acerta 3, 4, 5 ou 6 números ganha como prêmio, respectivamente, um “terno”, uma “quadra”, uma “quina” ou uma “sena”.

Nesta tarefa, você deve escrever um programa que diga qual foi o prêmio que Flavinho ganhou, 
dados os seis números que ele apostou e os seis números que foram sorteados.

Entrada
A entrada consiste de duas linhas apenas. 
Na primeira linha são dados seis números inteiros distintos entre 1 e 99, representando a aposta do Flavinho.
A segunda linha contém os seis números inteiros distintos sorteados.

Saída
Seu programa deve imprimir uma linha contendo uma palavra: “terno”, “quadra”, “quina” ou “sena”; 
caso Flavinho tenha acertado, respectivamente, 3, 4, 5, ou 6 números. 
Caso ele tenha acertado menos do que 3 números, imprima a palavra “azar”.
"""

######################################################################################################
   ##################################tratando as dezenas apostadas##################################
######################################################################################################
def examina_aposta():
    a,b,c,d,e,f = input("Informe os seis números inteiros distintos entre 1 e 99 apostados separados por espaço:").split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    aposta = [a,b,c,d,e,f]

    repetido = False #setado para True quando encontrar algum repetido
    distintos = False #setado para True quando nao encontrar nenhum numero repetido
    invalido = False #setado para True quando houve numero fora do range 1:99

    while(distintos != True):
        for contador in range(0, 6):
            #testando se a dezena pertence ao range 1:99
            if(aposta[contador]<1 or aposta[contador]>99):
                    invalido = True
            for contador2 in range(contador+1, 6):
                #if((aposta[contador2] == aposta[contador]) or (aposta[contador]<1 or aposta[contador]>99)): n da p usar pq a primeira posicao esta fora no for de dentro
                if(aposta[contador2] == aposta[contador]):
                    repetido = True
                contador2 += 1
            contador += 1
        if(invalido or repetido):
            a,b,c,d,e,f = input("Informe os seis números inteiros distintos entre 1 e 99 apostados separados por espaço:").split()
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(e)
            f = int(f)
            aposta = [a,b,c,d,e,f]
            repetido = False
            invalido = False
        else:
            distintos = True
    return aposta

######################################################################################################
   ##################################tratando as dezenas sorteadas##################################
######################################################################################################
def examina_sorteados():
    g,h,i,j,k,l = input("Informe os seis números inteiros distintos entre 1 e 99 sorteados separados por espaço:").split()
    g = int(g)
    h = int(h)
    i = int(i)
    j = int(j)
    k = int(k)
    l = int(l)
    sorteados = [g,h,i,j,k,l]

    repetido = False #setado para True quando encontrar algum repetido
    distintos = False #setado para True quando nao encontrar nenhum numero repetido
    invalido = False #setado para True quando houve numero fora do range 1:99

    while(distintos != True):
        for contador in range(0, 6):
            #testando se a dezena pertence ao range 1:99
            if(sorteados[contador]<1 or sorteados[contador]>99):
                    invalido = True
            for contador2 in range(contador+1, 6):
                #if((sorteados[contador2] == sorteados[contador]) or (sorteados[contador]<1 or sorteados[contador]>99)): n da p usar pq a primeira posicao esta fora no for de dentro
                if(sorteados[contador2] == sorteados[contador]):
                    repetido = True
                contador2 += 1
            contador += 1
        if(invalido or repetido):
            g,h,i,j,k,l = input("Informe os seis números inteiros distintos entre 1 e 99 sorteados separados por espaço:").split()
            g = int(g)
            h = int(h)
            i = int(i)
            j = int(j)
            k = int(k)
            l = int(l)
            sorteados = [g,h,i,j,k,l]
            repetido = False
            invalido = False
        else:
            distintos = True
    return sorteados

######################################################################################################
 ##################################logica para verificar os acertos##################################
######################################################################################################
def exibi_resultado(aposta, sorteados):
    acertos = 0

    for dezena_aposta in range(0, 6):
        for dezena_sorteados in range(0, 6):
            if(sorteados[dezena_sorteados] == aposta[dezena_aposta]):
                acertos += 1
            dezena_sorteados += 1
        dezena_aposta += 1

    dicionario = {1: "azar", 3: "terno", 4: "quadra", 5: "quina", 6: "sena"}

    if(acertos <3):
        print(dicionario[1])
    elif(acertos == 3):
        print(dicionario[3])
    elif(acertos == 4):
        print(dicionario[4])
    elif(acertos == 5):
        print(dicionario[5])
    else:
        print(dicionario[6])

if __name__ == "__main__":
    aposta = examina_aposta()
    sorteados = examina_sorteados()
    exibi_resultado(aposta, sorteados)
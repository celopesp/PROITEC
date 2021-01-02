def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("Movendo o disco", discos, "do", fp, "para", tp)

disco_invalido = False
while(disco_invalido == False): #N (0 ≤ N ≤ 30)
    cont_discos = discos = int(input("Informe a quantidade de discos de 1 a 30:"))
    if ((0<discos) and (discos<31)):
        disco_invalido = True

moveTower(discos,"pino1","pino2","pino3")
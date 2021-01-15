def valida_entrada(numero):
        try:
            int(numero)
        except ValueError:
            print(f'O 1° numero não é numérico voce entrou como o valor {n1}')
            exit(2)

n1 = int(input('Entre com o 1° numero que foi sorteado separados por espaço:'))


valida_entrada()
"""
Rolien e Naej são os desenvolvedores de um grande portal de programação. 
Para ajudar no novo sistema de cadastro do site, eles requisitaram a sua ajuda. 
Seu trabalho é fazer um código que valide as senhas que são cadastradas no portal, 
para isso você deve atentar aos requisitos a seguir:

    A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
    A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
    Além disso, a senha pode ter de 6 a 32 caracteres.

Entrada
A entrada contém vários casos de teste e termina com final de arquivo. Cada linha tem uma string S, 
correspondente a senha que é inserida pelo usuário no momento do cadastro.

Saída
A saída contém uma linha, que pode ser “Senha valida.”, 
caso a senha tenha cada item dos requisitos solicitados anteriormente, ou “Senha invalida.”, 
se um ou mais requisitos não forem atendidos.
"""
valido = False
while(valido == False):
    maiuscula = False
    minuscula = False
    numemero = False
    caracter_especial = False
    print("A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;")
    print("A senha não pode ter nenhum caractere de pontuação, acentuação ou espaço;")
    print("A senha pode ter de 6 a 32 caracteres.")
    entrada = input("Informe sua senha:")

    for contador in range(0, len(entrada)):
        if (entrada[contador].isupper()):
            maiuscula = True
        elif (entrada[contador].islower()):
            minuscula = True
        elif (entrada[contador].isnumeric()):
            numemero = True
        else:
            caracter_especial = True

    if(len(entrada)>5 and len(entrada)<33 and maiuscula == True and minuscula == True and numemero == True and caracter_especial == False):
        valido = True
        print('Senha válida.')
    else:
        print('Senha inválida.\n') #\n para quebra de linha para novo laço while
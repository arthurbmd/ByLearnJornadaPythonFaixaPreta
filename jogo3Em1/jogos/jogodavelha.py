def mostravelha():
    global lista
    cont = 1
    print('|-----|-----|-----|')
    for i in lista:
        print(f'|  {i}  ', end='') if cont % 3 != 0 else print(f'|  {i}  |\n|-----|-----|-----|')
        cont += 1


def mudajogador():
    global simb
    if simb == 'X':
        simb = 'O'
    else:
        simb = 'X'
    return simb


def jogar(simb, p):
    global lista
    mudou = False
    if lista[p] == p:
        lista[p] = simb
        mudou = True
    return mudou


def terminar():
    global lista
    fim = False
    #jogos em linha
    for i in range(0, 9, 3):
        if lista[i] == lista[i + 1] == lista[i + 2]:
            fim = True

    #jogos em coluna
    for i in range(3):
        if lista[i] == lista[i + 3] == lista[i + 6]:
            fim = True

    #jogos em diagonal
    diag = [0, 2]
    for i in diag:
        if i == 0:
            if lista[i] == lista[i + 4] == lista[i + 8]:
                fim = True
        else:
            if lista[i] == lista[i + 2] == lista[i + 4]:
                fim = True

    #jogos em velha
    ocor = 0
    for i in lista:
        if str(i) not in "XO":
            ocor += 1
    if ocor == 0:
        fim = True

    return fim


def inicio():
    global lista
    mostravelha()
    global simb
    terminou = False
    while not terminou:
        mudou = False
        while not mudou:
            po = int(input(f'Jogador "{simb}", qual posição quer jogar? '))
            mudou = jogar(simb, po)
            if not mudou:
                print('Jogada inválida')
        mudajogador()
        mostravelha()
        terminou = terminar()
    print('Fim')

lista = list(range(9))
simb = 'X'
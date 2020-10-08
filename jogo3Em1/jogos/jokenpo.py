from jogo3Em1.principal import leiaint
def jokenpo():
    from random import randint
    from time import sleep
    lista = ['Pedra', 'Papel', 'Tesoura']
    print('''Escolha entre:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    user = leiaint('Qual sua opção?:')
    pc = randint(0, 2)
    resultado = ' '
    if user == 0:
        if pc == 1:
            resultado = 'COMPUTADOR GANHOU!'
        elif pc == 2:
            resultado = 'JOGADOR GANHOU!'
    elif user == 1:
        if pc == 0:
            resultado = 'JOGADOR GANHOU!'
        elif pc == 2:
            resultado = 'COMPUTADOR GANHOU'
    elif user == 2:
        if pc == 0:
            resultado = 'COMPUTADOR GANHOU!'
        elif pc == 1:
            resultado = 'JOGADOR GANHOU!'
    else:
        print('Opção inválida, tente novamente!')

    if user == pc:
        resultado = 'EMPATOU!'
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    print('=' * 25)
    print('Jogador escolheu {}'.format(lista[user]))
    print('Computador escolheu {}'.format(lista[pc]))
    print('=' * 25)
    print(resultado)

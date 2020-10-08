# faça um programa que jogue par ou impar com o computador. o jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

def parouimpar():
    from random import randint
    cont = 0
    print('-' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR?')
    while True:
        print('-' * 30)
        num = int(input('Escolha um número: '))
        computador = randint(0, 10)
        escolha = ' '
        soma = computador + num
        while escolha not in 'PpIi':
            escolha = str(input('Você escolhe par ou ímpar? [P/I]'))
        print('-' * 30)
        print(f'O computador escolheu {computador} e você, {num}. Total de {soma}', end=' ')
        if soma % 2 == 0:
            print('DEU PAR.')
            print('-' * 30)
            if escolha in 'Pp':
                print('Você Venceu!')
                cont += 1
            else:
                print('Você Perdeu!')
                break
        else:
            print('DEU ÍMPAR.')
            print('-' * 30)
            if escolha in 'Ii':
                print('Você Venceu!')
                cont += 1
            else:
                print('Você Perdeu!')
                break
        print('Vamos jogar novamente...')
    print('-' * 30)
    print(f'GAME OVER! Você venceu {cont}', 'vezes.' if cont != 1 else 'vez.')

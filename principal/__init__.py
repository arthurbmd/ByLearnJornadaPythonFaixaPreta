
def menu():
    print('=' * 30)
    print('MENU DE JOGOS'.center(30))
    print('=' * 30)

    print('Quando jogo deseja jogar?')
    print('[1] Jogo da Velha')
    print('[2] Pedra, Papel ou Tesoura')
    print('[3] Jogo do Par ou Ímpar')
    print('[4] Jogo da Adivinhação')
    print('[5] Sair')
    print('[0] Menu principal')

    while True:
        resp = leiaint('Escolha uma opção válida: ')

        if resp in range(6):
            print('=' * 30)
            return resp
        else:
            print('Erro! Opção inválida!')


def continuar(resp=' '):
    while True:
        print('=' * 30)
        resp = str(input('Deseja continuar? '))
        if resp in 'SsNn':
            if resp in 'Ss':
                return True
            else:
                return False
        else:
            print('Resposta inválida!')


def leiaint(msg=''):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite apenas um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário interrompeu o programa.')
        else:
            break
    return int(n)

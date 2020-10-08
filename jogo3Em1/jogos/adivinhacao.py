# melhor o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer

def adivinhacao():

    from random import randint
    computador = randint(0, 10)
    tentativas = 1
    print('Vou pensar em um número entre 0 a 10. Tente adivinhar!')
    jogador = int(input('Em que número pensei? '))
    while jogador != computador:
        if jogador < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos...Tente novamente!')
        jogador = int(input('Em que número pensei? '))
        tentativas += 1
    print('Você acertou com {} tentativas.! Parabéns!'.format(tentativas))

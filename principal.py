# Menu de jogos
from jogo3Em1 import principal
from jogo3Em1.jogos import adivinhacao, parOuImpar, jokenpo, jogodavelha


resp = 0
while True:
    if resp == 0:
        resp = principal.menu()
        continue

    elif resp == 1:
        jogodavelha.inicio()

    elif resp == 2:
        jokenpo.jokenpo()

    elif resp == 3:
        parOuImpar.parouimpar()

    elif resp == 4:
        adivinhacao.adivinhacao()

    else:
        print('Saindo...')
        break

    continuar = principal.continuar()
    if not continuar:
        resp = 0
print('Obrigado por jogar! ')
print('Volte sempre!')

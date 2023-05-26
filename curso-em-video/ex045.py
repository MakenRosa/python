import random

jogador = int(input("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))

if jogador == 0:
    print("Você jogou PEDRA.")
elif jogador == 1:
    print("Você jogou PAPEL.")
elif jogador == 2:
    print("Você jogou TESOURA.")
else:
    print("Opção inválida. Tente novamente.")

computador = random.randint(0, 2)

if computador == 0:
    print("O computador jogou PEDRA.")
elif computador == 1:
    print("O computador jogou PAPEL.")
elif computador == 2:
    print("O computador jogou TESOURA.")

if jogador == 0:
    if computador == 0:
        print("EMPATE!")
    elif computador == 1:
        print("COMPUTADOR VENCE!")
    elif computador == 2:
        print("JOGADOR VENCE!")
elif jogador == 1:
    if computador == 0:
        print("JOGADOR VENCE!")
    elif computador == 1:
        print("EMPATE!")
    elif computador == 2:
        print("COMPUTADOR VENCE!")
elif jogador == 2:
    if computador == 0:
        print("COMPUTADOR VENCE!")
    elif computador == 1:
        print("JOGADOR VENCE!")
    elif computador == 2:
        print("EMPATE!")


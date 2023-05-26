import random

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
usuario = int(input('Qual é o seu palpite? '))
computador = random.randint(0, 10)
tentativas = 1

while usuario != computador:
    if usuario > computador:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    usuario = int(input('Qual é o seu palpite? '))
    tentativas += 1

print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

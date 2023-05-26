from random import randint
from time import sleep

print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)

jogos = []

while True:
    n = int(input('Quantos jogos você quer que eu sorteie? '))
    if n > 0:
        break
    else:
        print('Digite um número maior que 0!')

for i in range(n):
    jogos.append([])
    for j in range(6):
        while True:
            num = randint(1, 60)
            if num not in jogos[i]:
                jogos[i].append(num)
                break

for i in range(n):
    print(f'Jogo {i+1}: {sorted(jogos[i])}')
    sleep(1)

print('-'*30)
print('{:^30}'.format('BOA SORTE!'))
print('-'*30)

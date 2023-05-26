import random

jogadores = {'jogador1': random.randint(1, 6),'jogador2': random.randint(1, 6),'jogador3': random.randint(1, 6),'jogador4': random.randint(1, 6)}

ranking = list()

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    ranking.append((k, v))

ranking.sort(key=lambda item: item[1], reverse=True)

print('=-' * 30)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')


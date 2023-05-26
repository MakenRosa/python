jogadores = []

while True:
    jogador = {}
    gols = []

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)

for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')

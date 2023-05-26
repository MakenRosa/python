pessoas = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    opcao = input('Quer continuar? [S/N]: ')
    if opcao in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

maior = menor = pessoas[0][1]

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')



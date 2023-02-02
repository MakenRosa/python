matriz = [[], [], []]
soma_par = soma_terceira_coluna = maior_segunda_linha = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
        if i == 1:
            if j == 0:
                maior_segunda_linha = matriz[i][j]
            elif matriz[i][j] > maior_segunda_linha:
                maior_segunda_linha = matriz[i][j]
    print()

print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_segunda_linha}.')


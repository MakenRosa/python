valores = [[], []]

for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
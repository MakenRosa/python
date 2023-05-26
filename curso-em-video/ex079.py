valores = []

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')
print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

total = mais_de_mil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        mais_de_mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

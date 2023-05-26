numero = int(input('Digite um número: '))
cont = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\033[m')

print('O número {} foi divisível {} vezes'.format(numero, cont))
if cont == 2:
    print('O número {} é PRIMO'.format(numero))
else:
    print('O número {} NÃO É PRIMO'.format(numero))
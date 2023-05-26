valores = []

for i in range(0, 5):
    n = int(input('Digite um valor para a posição {}: '.format(i)))
    valores.append(n)

print('=-' * 30)
print('Você digitou os valores {}'.format(valores))

print('O maior valor digitado foi {} nas posições '.format(max(valores)), end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print('{}...'.format(i), end='')

print('\nO menor valor digitado foi {} nas posições '.format(min(valores)), end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print('{}...'.format(i), end='')
contador = 0
soma = 0

for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        contador += 1
        soma += i

print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))
soma_par = 0
cont_par = 0

for i in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma_par += num
        cont_par += 1

print('Você informou {} números PARES e a soma entre eles é {}'.format(cont_par, soma_par))
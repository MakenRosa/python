num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

lista = (num1, num2, num3, num4)

print(f'Você digitou os valores {lista}')

print(f'O valor 9 apareceu {lista.count(9)} vezes')

if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')


todos = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    todos.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'A lista completa é {todos}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

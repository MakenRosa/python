cont = 0
soma = 0
maior = 0
menor = 0
resposta = 'S'

while resposta in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print('Você digitou {} números e a média foi {}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

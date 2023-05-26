def sortear_valores():
    from random import randint
    from time import sleep
    print('-=' * 30)
    print('Sorteando 5 valores da lista: ', end='')
    lista = []
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.5)
    print('PRONTO!')
    return lista


def somar_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')


somar_pares(sortear_valores())
from time import sleep


def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.1)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            sleep(0.5)
    print('FIM!')


print('-=' * 20)
contagem(1, 10, 1)
print('-=' * 20)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
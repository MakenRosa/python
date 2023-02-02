def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except:
            print('Erro! Digite um número inteiro válido.')
            continue
        else:
            return n


def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except:
            print('Erro! Digite um número real válido.')
            continue
        else:
            return n

numInt = leiaInt()
numFloat = leiaFloat()
print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat}')
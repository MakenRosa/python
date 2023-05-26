import datetime


def vota(nascimento):
    idade = datetime.date.today().year - nascimento
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('Não pode votar')
    elif idade < 18 or idade > 65:
        print('Voto opcional')
    else:
        print('Voto obrigatório')


vota(int(input('Ano de nascimento: ')))

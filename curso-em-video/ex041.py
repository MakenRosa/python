import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento
print('O atleta tem {} anos.'.format(idade))
print('Classificação: ', end='')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')


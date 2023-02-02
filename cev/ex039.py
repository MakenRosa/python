import datetime

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

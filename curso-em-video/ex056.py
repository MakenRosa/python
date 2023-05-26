total_idade = 0
nome_velho = ''
idade_velho = 0
total_mulher_menos_de_20anos = 0

for i in range(1, 5):
    print('-' * 5 + ' {}ª PESSOA '.format(i) + '-' * 5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    total_idade += idade
    if i == 1 and sexo == 'M':
        nome_velho = nome
        idade_velho = idade
    if sexo == 'M' and idade > idade_velho:
        nome_velho = nome
        idade_velho = idade
    if sexo == 'F' and idade < 20:
        total_mulher_menos_de_20anos += 1

print('A média de idade do grupo é de {} anos.'.format(total_idade / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_velho, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_mulher_menos_de_20anos))

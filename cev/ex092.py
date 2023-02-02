pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['ano'] = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['contratação'] - pessoa['ano'] + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')

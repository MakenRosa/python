pessoas = []

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

soma = 0
for p in pessoas:
    soma += p['idade']

media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')

print('\nD) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')

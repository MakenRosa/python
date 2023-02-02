maior_de_idade = 0
total_homens = 0
total_mulheres_menos_de_20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior_de_idade += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_de_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior_de_idade}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {total_mulheres_menos_de_20} mulheres com menos de 20 anos')

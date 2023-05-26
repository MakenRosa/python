while True:
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'MF':
        break
    print('Dados inválidos. Tente novamente.')
print(f'Sexo {sexo} registrado com sucesso.')
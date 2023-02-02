pessoas = []
cont = 0

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    pessoas.append([cont, nome, [nota1, nota2], media])
    cont += 1
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, p in enumerate(pessoas):
    print(f'{i:<4}{p[1]:<10}{p[3]:>8.1f}')
print('-' * 26)

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(pessoas) - 1:
        print(f'Notas de {pessoas[opc][1]} são {pessoas[opc][2]}')
salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}'.format(salario, salario + aumento))
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc <= 25:
    print('Você está no PESO IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc <= 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA. Cuidado!')

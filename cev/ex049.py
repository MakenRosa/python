numero_para_tabuada = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero_para_tabuada, c, numero_para_tabuada * c))


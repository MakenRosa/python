valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha uma das opções abaixo:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}.'.format(valor1, valor2, valor1 + valor2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}.'.format(valor1, valor2, valor1 * valor2))
    elif opcao == 3:
        if valor1 > valor2:
            print('O maior valor entre {} e {} é {}.'.format(valor1, valor2, valor1))
        else:
            print('O maior valor entre {} e {} é {}.'.format(valor1, valor2, valor2))
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
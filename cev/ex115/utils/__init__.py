import os


def mostrar_menu():
    while True:
        print('-' * 30)
        print(f'{"MENU PRINCIPAL":^30}')
        print('-' * 30)
        print(f'{"1 - Ver pessoas cadastradas":<30}')
        print(f'{"2 - Cadastrar nova pessoa":<30}')
        print(f'{"3 - Sair do sistema":<30}')
        print('-' * 30)
        try:
            opcao = int(input('Sua opção: '))
            if opcao not in (1, 2, 3):
                print('Erro! Digite uma opção válida.')
                continue
        except:
            print('Erro! Digite um número inteiro válido.')
            continue
        else:
            if opcao == 1:
                mostrar_pessoas()
            elif opcao == 2:
                cadastrar_pessoa()
            elif opcao == 3:
                print('Saindo do sistema... Até logo!')
                break

def cadastrar_pessoa():
    print('-' * 30)
    print(f'{"NOVO CADASTRO":^30}')
    print('-' * 30)
    nome = input('Nome: ')
    idade = input('Idade: ')
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome:<30}{idade:>3} anos\n')


def mostrar_pessoas():
    print('-' * 50)
    print(f'{"PESSOAS CADASTRADAS":^50}')
    print('-' * 50)
    with open('pessoas.txt', 'r') as arquivo:
        for pessoa in arquivo:
            print(pessoa, end='')
    print('-' * 50)


def criar_arquivo_se_nao_existir():
    if not os.path.exists('pessoas.txt'):
        with open('pessoas.txt', 'w') as arquivo:
            arquivo.write('')
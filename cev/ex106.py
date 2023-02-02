def pedir_ajuda():
    while True:
        print('\033[0;33m', end='')
        ajuda = input('Função ou Biblioteca > ')
        print('\033[m', end='')
        if ajuda.upper() == 'FIM':
            break
        else:
            print('\033[0;34m', end='')
            help(ajuda)
            print('\033[m', end='')


pedir_ajuda()

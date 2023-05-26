def leiaDinheiro(msgm):
    while True:
        valor = input(msgm).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            return float(valor)
def print_formatado(palavra):
    print('~' * (len(palavra) + 5))
    print(f'  {palavra}')
    print('~' * (len(palavra) + 5))

print_formatado('Gustavo Guanabara')
print_formatado('Curso de Python no YouTube')
print_formatado('CeV')
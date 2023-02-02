expressao = input('Digite uma expressão: ')

if expressao.count('(') == expressao.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
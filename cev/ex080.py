valores_ordenados = []

for i in range(5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > valores_ordenados[-1]:
        valores_ordenados.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores_ordenados):
            if valor <= valores_ordenados[pos]:
                valores_ordenados.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores_ordenados}')
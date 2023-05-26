def definir_area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


area = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
definir_area(area, comprimento)
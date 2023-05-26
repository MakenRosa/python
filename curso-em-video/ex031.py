distancia = float(input("Qual a distância da viagem? "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preço da passagem é R$ {:.2f}".format(preco))

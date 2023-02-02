velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("Você foi multado! O valor da multa é de R${:.2f}".format((velocidade - 80) * 7))
else:
    print("Não foi multado!")

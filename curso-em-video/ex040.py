primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

print("A média é: ", (primeira_nota + segunda_nota) / 2)

if (primeira_nota + segunda_nota) / 2 >= 7:
    print("Aprovado")
elif (primeira_nota + segunda_nota) / 2 >= 5:
    print("Recuperação")
else:
    print("Reprovado")
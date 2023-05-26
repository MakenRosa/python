primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
terceiro_valor = int(input("Digite o terceiro valor: "))
#maior e menor valor
if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    maior_valor = primeiro_valor
elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior_valor = segundo_valor
else:
    maior_valor = terceiro_valor
if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    menor_valor = primeiro_valor
elif segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor_valor = segundo_valor
else:
    menor_valor = terceiro_valor

print("O maior valor é {}".format(maior_valor))
print("O menor valor é {}".format(menor_valor))



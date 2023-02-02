print("=" * 10 + "LOJAS MAKEN" + "=" * 10)

preco = float(input("Preço das compras: R$"))

opcao_pagamento = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? """))

if opcao_pagamento == 1:
    total = preco - (preco * 10 / 100)
elif opcao_pagamento == 2:
    total = preco - (preco * 5 / 100)
elif opcao_pagamento == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcela))
elif opcao_pagamento == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(total_parcelas, parcela))
else:
    total = preco
    print("Opção inválida de pagamento. Tente novamente.")

print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
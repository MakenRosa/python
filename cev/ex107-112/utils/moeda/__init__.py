def metade(preco):
    res = preco / 2
    return formatar(res)


def dobro(preco):
    res = preco * 2
    return formatar(res)


def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return formatar(res)


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return formatar(res)

def formatar(preco):
    res = f'R${preco:.2f}'.replace('.', ',')
    return res


def resumo(preco, aumento, reducao):
    print(f'A metade de {formatar(preco)} é {metade(preco)}')
    print(f'O dobro de {formatar(preco)} é {dobro(preco)}')
    print(f'Aumentando 10%, temos {aumentar(preco, aumento)}')
    print(f'Diminuindo 13%, temos {diminuir(preco, reducao)}')

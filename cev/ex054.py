import datetime

maior = 0
menor = 0

for i in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = datetime.date.today().year - ano_nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
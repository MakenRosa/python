print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
termos_adicionais = 10
cont = 1
numero_total_de_termos = 0

while termos_adicionais != 0:
    print('{} -> '.format(termo), end='')
    numero_total_de_termos += 1
    termo += razao
    cont += 1
    if cont > termos_adicionais:
        print('PAUSA')
        termos_adicionais = int(input('Deseja mostrar mais quantos termos? '))
        cont = 1

print('Progressão finalizada com {} termos mostrados.'.format(numero_total_de_termos))
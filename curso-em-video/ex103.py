def cadastrar_jogador(nome='<desconhecido>', gols='0'):
    """
    -> Cadastra um jogador.
    :param nome: (Opcional) Nome do jogador.
    :param gols: (Opcional) Número de gols.
    :return: Dicionário com os dados do jogador.
    """
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    jogador = {'nome': nome, 'gols': gols}
    return jogador


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
jogador = cadastrar_jogador(nome, gols)
print(f'O jogador {jogador["nome"]} fez {jogador["gols"]} gol(s) no campeonato.')

from utils import moeda
from utils import dados

p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
#
# Created by Pedro Freitas on 14/01/2020.
#

brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athetico-PR',
		      'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
		      'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
		      'Ceará-SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')

print(f'\033[1;37mO G5 do Brasileirão 2019 foi: {brasileirao[0:5]}\n')
print(f'\033[1;37mO Z4 do Brasileirão 2019 foi: {brasileirao[16:]}\n')
print(f'\033[1;37mEm Ordem Alfabética a tabela do Brasileirão ficaria:\n{sorted(brasileirao)}\n')
print(f'\033[1;37mA Chapecoense terminou o Brasileirão na {brasileirao.index("Chapecoense") + 1}º posição.')
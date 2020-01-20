#
# Created by Pedro Freitas on 20/01/2020.
#

def ficha(nome = '<desconhecido>', gols = '0'):
	return f'O jogador {nome} fez um total de {gols} gol(s) no campeonato.'

name = str(input('Digite o nome de jogador: '))
gol = str(input('Digite o total de gols marcados por ele: '))

if gol.isnumeric():
	gol = int(gol)
else:
	gol = 0

if name.strip() == '':
	print(ficha(gols = gol))
else:
	print(ficha(name, gol))
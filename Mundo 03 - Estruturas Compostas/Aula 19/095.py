#
# Created by Pedro Freitas on 16/01/2020.
#

aproveitamento = {}
matches = []
jogadores = []
totalGols = 0

while True:

	nome = str(input('Nome do jogador: '))
	partidas = int(input(f'Total partidas jogadas: '))

	aproveitamento['nome'] = nome
	aproveitamento['partidas'] = partidas

	for p in range(1, (partidas + 1)):
		gols = int(input(f'Quantidade de gols na {p}ª partida: '))
		matches.append(gols)
		totalGols += gols

	aproveitamento['gols'] = matches[:]
	aproveitamento['maxGols'] = totalGols

	jogadores.append(aproveitamento.copy())
	
	aproveitamento.clear()
	matches.clear()
	totalGols = 0

	resposta = str(input('Deseja continuar? [S/N] ')).upper()
	
	if resposta != 'S':
		break
print('=='*45)
print(f'{"Nome":<10}     {"Partidas":<10}     {"Gols por Partida"}     {"Total de Gols":<10}')

for k, v in enumerate(jogadores):
	print(f'{v["nome"]:<10}     {v["partidas"]:<10}     {v["gols"]}     {v["maxGols"]:>10}')
print('=='*45)

show = 0
while show != -1:
	show = int(input('Digite o indice do jogador [a partir do zero] no qual deseja ver o aproveitamento individual: '))

	for i, r in enumerate(jogadores):
		if show == i:
			print(f'{r["nome"]} teve o seguinte aproveitamento: ')
			for k, v in enumerate(r['gols']):
				print(f'Na {k + 1}ª partida fez um total de {v} gols.')
#
# Created by Pedro Freitas on 16/01/2020.
#

aproveitamento = {}
matches = []
totalGols = 0

nome = str(input('Nome do jogador: '))
partidas = int(input(f'Total partidas jogadas: '))

aproveitamento['nome'] = nome
aproveitamento['partidas'] = partidas

for p in range(1, (partidas + 1)):
	gols = int(input(f'Quantidade de gols na {p}ª partida: '))
	matches.append(gols)
	totalGols += gols

aproveitamento['gols'] = matches
aproveitamento['maxGols'] = totalGols

print(f'{aproveitamento["nome"]} jogou um total de {aproveitamento["partidas"]} partidas e teve o seguinte aproveitamento: ')

for k, v in enumerate(list(aproveitamento['gols'])):
	print(f'Na {k + 1}ª partida marcou {v} gol(s)')

print(f'No final dessa sequência de jogos {aproveitamento["nome"]} marcou um total de {aproveitamento["maxGols"]} gols.')
#
# Created by Pedro Freitas on 15/01/2020.
#

from random import randint
from operator import itemgetter
from time import sleep

jogador = {}
ordenado = {}

for d in range(1, 5):
	jogada = randint(1, 6)
	jogador[f'Jogador {d}'] = jogada
	print(f'O {d}º jogador tirou {jogada}.')

	sleep(1)

print('_'*30,end='')
print()

ordenado = sorted(jogador.items(), key = itemgetter(1), reverse = True)

for j, n in enumerate(ordenado):
	print(f'{j + 1}º lugar: {n[0]} com {n[1]}')
	sleep(1)
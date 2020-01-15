#
# Created by Pedro Freitas on 15/01/2020.
#

from random import randint
from time import sleep

jogos = int(input('\033[1;37mDigite o número de jogos que você pretende jogar: '))

bilheteAtual = list() 
totalBilhetes = list()

for j in range(0, jogos): # para uma quantidade de 'n' jogos
	for n in range(0, 6): # sorteio 6 numeros, entre 1 e 60 e 'marco' o numero no bilhete
		numero = randint(1, 60)
		if numero not in bilheteAtual:
			bilheteAtual.append(numero)

	totalBilhetes.append(bilheteAtual[:])
	bilheteAtual.clear()

print(f'Você marcou um total de {jogos} bilhetes. Segue os seus jogos:')
for pos, b in enumerate(totalBilhetes):
	print(f'Jogo {pos + 1}: {b}')
	sleep(1)
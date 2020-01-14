#
# Created by Pedro Freitas on 14/01/2020.
#

from random import randrange

tupla = (randrange(100), randrange(200), randrange(300), randrange(400), randrange(500))

menor = maior = tupla[0]

for n in range(0, 5):
	if (tupla[n] > maior):
		maior = tupla[n]
	elif (tupla[n] < menor):
		menor = tupla[n]

print(f'\033[1;37mOs números gerados foram {tupla}. Dentre esses o MAIOR é {maior} e o MENOR é {menor}.')
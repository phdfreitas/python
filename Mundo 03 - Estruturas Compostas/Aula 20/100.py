#
# Created by Pedro Freitas on 19/01/2020.
#

from random import randint
from time import sleep

def sorteia(lista):
	print('Sorteando 5 valores para a lista: ', end = '')
	for x in range(0, 5):
		n = randint(0, 1000)
		print(f'{n} ', end = '', flush = True)
		sleep(0.5)
		lista.append(n)
		
def somaPar(lista):
	soma = 0
	for par in lista:
		if par % 2 == 0:
			soma += par
	print(f'\nA lista de números informada foi {lista} a soma dos números pares é igual a {soma}')

numeros = list()

sorteia(numeros)
somaPar(numeros)
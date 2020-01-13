#
# Created by Pedro Freitas on 13/01/2020.
#

from time import sleep

n = int(input('\033[1;37mDigite um número inteiro: '))
print('Calculando o fatorial de {}...'.format(n))

fatorial = 1

while n > 0:
	fatorial = fatorial * n
	n -= 1

sleep(2)
print('Resultado: {}'.format(fatorial))
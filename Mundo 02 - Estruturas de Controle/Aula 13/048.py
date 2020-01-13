#
# Created by Pedro Freitas on 11/01/2020.
#

soma = 0
for c in range(1, 500):
	if c % 3 == 0 and c % 2 != 0:
		soma += c
print('\033[1;37mA soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é: {}.'.format(soma))
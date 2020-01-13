#
# Created by Pedro Freitas on 11/01/2020.
#

soma = 0
print('\033[1;33mVocê deve digitar seis números inteiros.')
for c in range(1, 7):
	n = int(input('{}º número: '.format(c)))
	if n % 2 == 0:
		soma += n
print('A soma dos números pares dentre os 6 números informados resulta em: {}'.format(soma))
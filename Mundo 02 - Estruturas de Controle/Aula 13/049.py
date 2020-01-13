#
# Created by Pedro Freitas on 11/01/2020.
#

n = int(input('\033[1;32mDigite um número inteiro: '))

print('A tabuada de {} é: '.format(n))

for c in range(1, 11):
	print('{} x {:2} = {}'.format(n, c, (n * c)))
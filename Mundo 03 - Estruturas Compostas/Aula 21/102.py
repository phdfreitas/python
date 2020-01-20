#
# Created by Pedro Freitas on 20/01/2020.
#

def fatorial(numero, show = 'N'):
	fat = 1
	for f in range(numero, 0, -1):
		if show == 'S':
			if f > 1:
				print(f'{f} x ', end = '')
			else:
				print('1 = ', end = '')
		fat = fat * f
	
	return fat

num = int(input('Digite um número para calcular seu fatorial: '))
sn = str(input('Você deseja ver o processo do cálculo? [S/N] ')).upper()

print(fatorial(num, sn))
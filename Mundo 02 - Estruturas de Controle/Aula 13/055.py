#
# Created by Pedro Freitas on 11/01/2020.
#

maior = 0
menor = 0

for c in range(0,5):
	peso = float(input('\033[1;33mDigite o peso em Kg: '))
	if c == 0:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		elif peso < menor:
			menor = peso
print('O MAIOR peso é {:.1f}kg e O MENOR é {:.1f}kg'.format(maior, menor))
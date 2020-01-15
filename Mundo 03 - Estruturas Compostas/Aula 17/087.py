#
# Created by Pedro Freitas on 15/01/2020.
#

matriz = [[],[],[]]

sPares = 0
sTC = 0
maior = 0

for x in range(0,3):
	for y in range(0, 3):
		matriz[x].append(int(input('\033[1;37mNúmero: ')))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for x in range(0,3):
	print('[ ',end='')
	for y in range(0, 3):
		print(f'{matriz[x][y]} ',end='')
	print(']')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for x in range(0,3):
	for y in range(0, 3):
		if (matriz[x][y] % 2 == 0):
			sPares += matriz[x][y]
		if (y == 2):
			sTC += matriz[x][y]
		if (x == 1):
			if y == 0:
				maior = matriz[x][y]
			else:
				if matriz[x][y] > maior:
					maior = matriz[x][y]

print(f'A soma de todos os números pares da matriz é igual a {sPares}.')
print(f'A soma de todos os números da terceira coluna é igual a {sTC}.')
print(f'O MAIOR valor da 2ª linha é igual a {maior}.')
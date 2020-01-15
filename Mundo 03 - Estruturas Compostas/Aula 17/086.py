#
# Created by Pedro Freitas on 15/01/2020.
#

matriz = [[],[],[]]

for x in range(0,3):
	for y in range(0, 3):
		matriz[x].append(int(input('\033[1;37mNúmero: ')))

for x in range(0,3):
	print('[ ',end='')
	for y in range(0, 3):
		print(f'{matriz[x][y]} ',end='')
	print(']')
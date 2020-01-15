#
# Created by Pedro Freitas on 15/01/2020.
#

numeros = [[],[]]

for x in range(0, 7):
	num = int(input('\033[1;37mNúmero: '))

	if num % 2 == 0:
		numeros[0].append(num)
	else:
		numeros[1].append(num)

print(f'Os números pares digitados foram: {numeros[0]}.\nEm ordem crescente eles ficam:')
numeros[0].sort()
print(f'{numeros[0]}')

print(f'Os números ímpares digitados foram: {numeros[1]}.\nEm ordem crescente eles ficam:')
numeros[1].sort()
print(f'{numeros[1]}')
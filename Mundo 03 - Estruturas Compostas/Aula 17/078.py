#
# Created by Pedro Freitas on 14/01/2020.
#

lista = []
maior = menor = 0

for x in range(0, 5):
	lista.append(int(input(f'\033[1;37mDigite o {x + 1}º número: ')))

	if lista[x] > maior:
		maior = lista[x]
	elif lista[x] < menor:
		menor = lista[x]

posMaior = posMenor = -1
print(f'O MAIOR número é {maior} e está nas posições: ', end='')

for p, v in enumerate(lista):
	if v == maior:
		print(f'{p}', end=' ')

print(f'\nO MENOR número é {menor} e está nas posições: ', end='')

for p, v in enumerate(lista):
	if v == menor:
		print(f'{p}', end=' ')
print()
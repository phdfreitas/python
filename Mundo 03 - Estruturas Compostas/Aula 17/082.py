#
# Created by Pedro Freitas on 14/01/2020.
#

lista = []

while True:
	lista.append(int(input('\033[1;37mDigite um número: ')))

	resposta = str(input('Você deseja continuar? [S/N] ')).upper()
	while resposta not in 'SN':
		resposta = str(input('Algo deu errado, tente novamente. Você deseja continuar? [S/N] ')).upper()

	if resposta != 'S':
		break

pares = []
impares = []

for item in lista:
	if item % 2 == 0:
		pares.append(item)
	else:
		impares.append(item)

print(f'A lista total é {lista}.\nOs números pares são: {pares}\nE os números impares são: {impares}.')
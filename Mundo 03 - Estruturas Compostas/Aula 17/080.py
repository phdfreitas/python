#
# Created by Pedro Freitas on 14/01/2020.
#

lista = []

for e in range(0, 5):
	numero = int(input('\033[1;33mDigite um número: '))
	
	if len(lista) == 0 or numero > lista[-1]:
		lista.append(numero)
	else:
		for i in range(0, len(lista)):
			if numero < lista[i]:
				lista.insert(i,numero)
				break
print(f'A lista ordenada é igual a {lista}')
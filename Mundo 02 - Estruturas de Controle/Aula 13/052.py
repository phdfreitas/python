#
# Created by Pedro Freitas on 11/01/2020.
#

numero = int(input('\033[1;33mDigite um número inteiro: '))

contador = 0

for c in range(1, (numero + 1)):
	if numero % c == 0:
		contador += 1
if contador == 2:
	print('O número informado foi {} e esse número É PRIMO!'.format(numero))
else:
	print('O número informado foi {} e esse número NÃO É PRIMO!'.format(numero)) 
#
# Created by Pedro Freitas on 09/01/2020.
#

n1 = int(input('\033[1;33mDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
	print('O primeiro valor é o maior.')
elif n2 > n1:
	print('O segundo valor é o maior.')
else:
	print('Não existe valor maior, os dois são iguais.')
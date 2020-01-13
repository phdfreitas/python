#
# Created by Pedro Freitas on 13/01/2020.
#

n = 0
soma = 0
total = 0

while n != 999:
	total += 1

	n = float(input('\033[1;37mDigite um número: '))
	soma += n
print('O total de números digitados incluindo o 999 foi {}'.format(total))
print('A soma de todos os números digitados foi {}'.format(abs(soma - 999)))
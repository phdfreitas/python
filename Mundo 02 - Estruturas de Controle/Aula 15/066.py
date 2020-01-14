#
# Created by Pedro Freitas on 13/01/2020.
#

soma = total = 0
while True:
	n = int(input('Digite um número: '))

	if n == 999:
		break
	total += 1
	soma += n
	
print(f'A soma dos {total} números digitados é igual a {soma}.')
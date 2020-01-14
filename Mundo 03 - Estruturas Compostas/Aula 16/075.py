#
# Created by Pedro Freitas on 14/01/2020.
#

n1 = int(input('\033[1;37mDigite um número: '))
n2 = int(input('\033[1;37mDigite um número: '))
n3 = int(input('\033[1;37mDigite um número: '))
n4 = int(input('\033[1;37mDigite um número: '))

tupla = (n1, n2, n3, n4)

print(f'O número 9 aparece um total de {tupla.count(9)} vezes.')

if tupla.count(3) != 0:
	print(f'O primeiro número 3 está na {tupla.index(3)}º posição.')
else:
	print(f'Não existe qualquer valor 3 na tupla.')

par = 0
for pos, val in enumerate(tupla):
	if val % 2 == 0:
		par += 1
print(f'Foi digitado um total de {par} números pares.')
#
# Created by Pedro Freitas on 11/01/2020.
#

first = int(input('\033[1;33mDigite o primeiro termo da PA: '))
razao = int(input('Agora, informe a razão dessa PA: '))

intervalo = (razao * 10) + first

for c in range(first, intervalo, razao):
	print('{} '.format(c), end='')
print()
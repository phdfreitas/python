#
# Created by Pedro Freitas on 13/01/2020.
#

first = int(input('\033[1;37mDigite o primeiro termo da PA: '))
razao = int(input('Agora, informe a razão dessa PA: '))

intervalo = (razao * 10) + first

while first < intervalo:
	print(first, end=' ')
	first += razao
print()
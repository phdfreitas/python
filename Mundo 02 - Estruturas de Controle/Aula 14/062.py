#
# Created by Pedro Freitas on 13/01/2020.
#

first = int(input('\033[1;37mDigite o primeiro termo da PA: '))
razao = int(input('Agora, informe a razão dessa PA: '))

intervalo = (razao * 10) + first

contador = 0
resposta = 10

while first < intervalo:
	contador += 1

	print(first, end=' ')
	first += razao

	if contador == resposta:
		contador = 0
		resposta = int(input('\nQuantos termos a mais você deseja ver? '))
		intervalo = (razao * resposta) + first
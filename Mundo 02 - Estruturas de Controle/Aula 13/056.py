#
# Created by Pedro Freitas on 11/01/2020.
#

totalIdades = 0
totalWomen = 0

oldMan = ''
auxOldMan = 0

for c in range(1, 5):
	print('\033[1;33m{}º Pessoa:'.format(c))
	nome = str(input('Digite o seu nome: '))
	idade = int(input('Digite sua idade: '))
	sexo = str(input('Digite o seu sexo [M/F]: ')).upper()

	totalIdades += idade

	if sexo == 'M':
		if idade > auxOldMan:
			oldMan = nome
			auxOldMan = idade
	elif sexo == 'F' and idade < 20:
		totalWomen += 1
	print()

print('A média de idade do grupo é de {} anos.'.format(totalIdades / 4))
print('O homem mais velho do grupo é {} e ele tem {} anos.'.format(oldMan, auxOldMan))
print('No grupo, {} mulheres tem menos de 20 anos.'.format(totalWomen))
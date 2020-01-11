#
# Created by Pedro Freitas on 09/01/2020.
#

from datetime import date

anoAtleta = int(input('\033[1;33mInforme o ano em que você nasceu: '))

idade = (date.today().year) - anoAtleta

print('Atualmente você tem {} anos e está classificado como:'.format(idade))

if idade <= 9:
	print('MIRIM')
elif idade > 9 and idade <= 14:
	print('JUVENIL')
elif idade > 14 and idade <= 19:
	print('JÚNIOR')
elif idade > 19 and idade <= 25:
	print('SÊNIOR')
else:
	print('MASTER')
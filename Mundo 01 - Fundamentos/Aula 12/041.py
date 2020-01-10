#
# Created by Pedro Freitas on 09/01/2020.
#

from datetime import date

anoAtual = date.today().year

anoAtleta = int(input('Informe o ano em que você nasceu: '))

idade = anoAtual - anoAtleta

if idade <= 9:
	print('MIRIM')
elif idade > 9 and idade <= 14:
	print('JUVENIL')
elif idade > 14 and idade <= 19:
	print('JÚNIOR')
else:
	print('MASTER')
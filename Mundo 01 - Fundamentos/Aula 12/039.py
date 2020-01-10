#
# Created by Pedro Freitas on 09/01/2020.
#

from datetime import date

anoAtual = date.today().year

anoNasc = int(input('Digite o ano em que você nasceu: '))

if anoAtual - anoNasc == 18:
	print('Você deve se alistar esse ano.')
elif anoAtual - anoNasc > 18:
	rest = (anoAtual - anoNasc) - 18
	print('Já passou da hora do seu alistamento. Se você não se alistou, deveria ter feito isso há {} ano(s).'.format(rest))
else:
	rest = 18 - (anoAtual - anoNasc)
	print('Ainda não é o momento do seu alistamento. Você deve se alistar em {} ano(s).'.format(rest))
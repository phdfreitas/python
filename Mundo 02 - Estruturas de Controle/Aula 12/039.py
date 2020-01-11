#
# Created by Pedro Freitas on 09/01/2020.
#

from datetime import date

anoAtual = date.today().year

anoNasc = int(input('\033[1;33mDigite o ano em que você nasceu: '))

idade = anoAtual - anoNasc
total = abs((anoAtual - anoNasc) - 18)

print('Atualmente você tem {} anos, logo:'.format(idade))

if anoAtual - anoNasc == 18:
	print('Você deve se alistar esse ano.')
elif anoAtual - anoNasc > 18:
	print('Já passou da hora do seu alistamento. Se você não se alistou, deveria ter feito isso há {} ano(s).'.format(total))
else:
	print('Ainda não é o momento do seu alistamento. Você deve se alistar em {} ano(s).'.format(total))
#
# Created by Pedro Freitas on 08/01/2020.
#

year = int(input('Enter the year: '))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
	print('Bissexto.')
else:
	print('Não é bissexto.')
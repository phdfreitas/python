#
# Created by Pedro Freitas on 08/01/2020.
#

distance = float(input('Enter the distance: '))

if distance <= 200:
	print('It will cost R$ {:.2f}'.format(distance * 0.5))
else:
	print('It will cost R$ {:.2f}'.format(distance * 0.45))
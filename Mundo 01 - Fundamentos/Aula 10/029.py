#
# Created by Pedro Freitas on 08/01/2020.
#

speed = float(input('Enter car speed: '))

if speed > 80:
	print('You have been fined and must pay $ {:.2f}'.format((speed - 80) * 7))
else:
	print('Keep going.')
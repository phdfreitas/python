#
# Created by Pedro Freitas on 08/01/2020.
#

n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))
n3 = float(input('Enter third number: '))

if n1 >= n2 and n1 >= n3:
	print('MAIOR: {}'.format(n1))
if n2 > n1 and n2 >= n3:
	print('MAIOR: {}'.format(n2))
if n3 > n1 and n3 > n2:
	print('MAIOR: {}'.format(n3))
if n1 <= n2 and n1 <= n3:
	print('MENOR: {}'.format(n1))
if n2 < n1 and n2 <= n3:
	print('MENOR: {}'.format(n2))
if n3 < n1 and n3 < n2:
	print('MENOR: {}'.format(n3))
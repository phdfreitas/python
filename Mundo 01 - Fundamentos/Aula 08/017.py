#
# Created by Pedro Freitas on 05/01/2020.
#

from math import sqrt

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

h = sqrt((co**2) + (ca**2))

print('O valor da hipotenusa é: {:.2f}.'.format(h))
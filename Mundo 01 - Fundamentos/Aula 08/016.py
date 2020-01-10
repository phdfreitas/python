#
# Created by Pedro Freitas on 05/01/2020.
#

from math import trunc

n = float(input('Digite um número com algumas casas após a vírgula: '))
print('A parte inteira de {} é {}.'.format(n, trunc(n)))
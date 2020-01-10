#
# Created by Pedro Freitas on 08/01/2020.
#

name = str(input('Please, enter your name: '))

cutName = name.split()

print('First Name: {}\nLast Name {}'.format(cutName[0], cutName[len(cutName) - 1]))
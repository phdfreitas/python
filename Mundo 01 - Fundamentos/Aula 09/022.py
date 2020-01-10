#
# Created by Pedro Freitas on 07/01/2020.
#

name = str(input('Please, type your name: '))

cutName = name.split()

print('Upper: {}\nLower {}'.format(name.upper(), name.lower()))
print('Length: {}'.format(len(name.replace(' ', ''))))
print('Split & Length: {}'.format(len(cutName[0])))
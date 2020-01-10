#
# Created by Pedro Freitas on 05/01/2020.
#

from random import sample

a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))

ordem = sample([a1, a2, a3, a4], k = 4)

print('A ordem de apresentação é: {}.'.format(ordem))
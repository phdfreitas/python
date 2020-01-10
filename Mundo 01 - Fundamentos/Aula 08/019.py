#
# Created by Pedro Freitas on 05/01/2020.
#

from random import choice

a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))

s = choice([a1, a2, a3, a4])

print('{} vai apagar o quadro.'.format(s))
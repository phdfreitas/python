#
# Created by Pedro Freitas on 07/01/2020.
#

num = int(input('Enter a *integer* number [0,9999]: '))

u = (num % 10)
d = ((num - u) % 100) // 10
c = (((num % 1000) - (num % 100)) // 100)
m = num // 1000

print('Milhar {}\nCentena {}\nDezena {}\nUnidade {}'.format(m, c, d, u))  
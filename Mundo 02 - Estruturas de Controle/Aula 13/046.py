#
# Created by Pedro Freitas on 11/01/2020.
#

from datetime import date
from time import sleep

print('\033[1;36mContagem regressiva para o ano novo!!\n')
for c in range(10, 0, -1):
	print('{} ...'.format(c))
	sleep(1)
print('\nFELIZ {}!!!'.format(date.today().year))
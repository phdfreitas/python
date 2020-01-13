#
# Created by Pedro Freitas on 11/01/2020.
#

from datetime import date

totalDZ = 0
totalMN = 0

for c in range(0, 7):
	nasc = int(input('\033[1;33mDigite o ano de nascimento: '))
	if date.today().year - nasc >= 18:
		totalDZ += 1
	else:
		totalMN += 1
print('{} pessoa(s) já é/são maior(es) de idade e {} pessoa(s) não é/são.'.format(totalDZ, totalMN))
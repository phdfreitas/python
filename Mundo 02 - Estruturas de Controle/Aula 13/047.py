#
# Created by Pedro Freitas on 11/01/2020.
#

for c in range(0, 52, 2):
	if c % 10 == 2 and c != 2:
		print()
	if c != 0:
		print('\033[1;36m{} '.format(c), end='')
print()
#
# Created by Pedro Freitas on 13/01/2020.
#

while True:
	n = int(input('\033[1;37mDigite um número para saber sua tabuada: '))
	
	if n < 0:
		break
	for c in range(1, 11):
		print(f'{n} x {c:2} = {n * c}')